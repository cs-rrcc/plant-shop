"""
Author(s): Andrew, Kobe, and Mckenna
Description:
"""


from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy.exc import SQLAlchemyError as SQL_Execution_Error
from datetime import datetime
import pytz
import bcrypt

from app import app, db
from app.auth import role_required
from app.forms import CategoryViewForm, LoginForm, PlantForm, SignUpForm
from app.models import (
    Cart,
    CartItem,
    CartStatus,
    Order,
    OrderItem,
    Plant,
    User,
    UserRole
)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data != form.password_confirmation.data:
            flash("Passwords do not match!", "Error")
            return redirect(url_for('signup'))
        try:
            user = User(
                name=form.name.data,
                email=form.email.data.strip().lower(),
                password=bcrypt.hashpw(
                    form.password.data.encode("utf-8"),
                    bcrypt.gensalt()),
                role=UserRole(form.role.data)
                )

            db.session.add(user)
            db.session.commit()

            flash("Account created", "Success")
            return redirect(url_for('login'))

        except (ValueError, SQL_Execution_Error):
            db.session.rollback()
            flash("Something Went Wrong Creating Your Account", "Error")
            return redirect(url_for('error_page'))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.checkpw(
            form.password.data.encode("utf-8"),
            user.password
        ):
            login_user(user)

            if user.role.value == 'horticulturist':
                return redirect(url_for('seller_dashboard'))
            return redirect(url_for('customer_dashboard'))
        else:
            flash("Invalid email or password", "Error")

    return render_template('login.html', form=form)


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Successfully logged out", "Success")
    return redirect(url_for('index'))


def get_all_plant_listings():
    return Plant.query.filter(Plant.quantity > 0).all()


def get_plants_by_seller(seller_id: int):
    return (
        Plant.query.filter_by(seller_id=seller_id)
        .order_by(Plant.quantity.asc())
        .all()
    )


def get_plants_by_category(variety: str, climate: str):
    plant_list_query = Plant.query.filter(Plant.quantity > 0)

    if variety != 'all':
        plant_list_query = plant_list_query.filter(
            Plant.variety == variety
        )

    if climate != 'all':
        plant_list_query = plant_list_query.filter(
            Plant.climate == climate
        )

    return plant_list_query.all()


@app.route('/buyplants', methods=['GET', 'POST'])
@login_required
@role_required('customer')
def customer_dashboard():
    form = CategoryViewForm()
    listings = get_all_plant_listings()

    if form.validate_on_submit():
        try:
            listings = get_plants_by_category(
                form.variety.data,
                form.climate.data
            )
        except (SQL_Execution_Error):
            return redirect(url_for('error_page'))

    return render_template(
        'customer_dashboard.html',
        listings=listings,
        form=form
    )


def get_or_create_cart(user):
    cart = Cart.query.filter_by(
        customer_id=user.id,
        status=CartStatus.ACTIVE
    ).first()

    if cart is None:
        cart = Cart(
            customer=user,
            status=CartStatus.ACTIVE
        )
        db.session.add(cart)
        db.session.flush()  # ensure cart.id exists

    return cart


def check_plant_quantity(plant_id: int, requested_qty: int):
    """
    Check if a plant exists and if the requested quantity is valid.
    """
    plant = Plant.query.get(plant_id)

    if plant is None:
        return None, False, "Plant not found."

    if requested_qty <= 0:
        return plant, False, "Quantity must be at least 1."

    if plant.quantity < requested_qty:
        return plant, False, f"Only {plant.quantity} left in stock."

    return plant, True, ""


def add_or_manage_cart_item(cart, plant_id: int, quantity: int):
    plant = Plant.query.filter_by(id=plant_id).first()
    cart_item = CartItem.query.filter_by(
        cart_id=cart.id,
        plant_id=plant.id
    ).first()

    # See if this plant is already in the cart
    if cart_item:
        new_quantity = cart_item.quantity + quantity

        # Make sure the total in cart does not exceed stock
        if new_quantity > plant.quantity:
            remaining = plant.quantity - cart_item.quantity
            if remaining <= 0:
                return (
                    False,
                    "You already have the maximum available quantity of "
                    "this plant in your cart."
                )
            else:
                return (
                    False,
                    f"You can only add {remaining} more of this plant."
                )

        cart_item.quantity = new_quantity
    else:
        cart_item = CartItem(
            cart=cart,
            plant=plant,
            quantity=quantity
        )
        db.session.add(cart_item)
    return True, None


@app.route('/mycart/add', methods=['POST'])
@login_required
@role_required('customer')
def add_to_cart():
    # Parse input
    try:
        plant_id = int(request.form.get("plant_id"))
        quantity = int(request.form.get("quantity", 1))
    except (TypeError, ValueError):
        flash("Invalid quantity selected.", "Error")
        return redirect(url_for("customer_dashboard"))

    # Validate against stock
    plant, ok, message = check_plant_quantity(plant_id, quantity)
    if not ok:
        flash(message, "Error")
        return redirect(url_for("customer_dashboard"))

    # Get or create the user's cart
    cart = get_or_create_cart(current_user)

    # Add to cart or update the quantity of an item in the cart
    ok, message = add_or_manage_cart_item(cart, plant_id, quantity)
    if not ok:
        flash(message, "Error")
        return redirect(url_for("customer_dashboard"))

    db.session.commit()
    flash(f"Added {quantity} × {plant.name} to your cart.", "Success")
    return redirect(url_for("customer_dashboard"))


def validate_cart_items_in_cart(cart):
    for item in cart.cart_items:
        if item.plant.quantity < item.quantity:
            return (
                False,
                f"Not enough stock left for {item.plant.name}. "
                f"Removing {item.plant.name} to its stock amount"
            )
    return True, None


def fix_item_quantity_before_checkout(cart):
    for item in cart.cart_items:
        if item.quantity > item.plant.quantity:
            item.quantity = item.plant.quantity


@app.route('/mycart', methods=['GET'])
@login_required
@role_required('customer')
def view_cart():

    cart = current_user.cart

    if cart is None or not cart.cart_items:
        return render_template("view_cart.html", cart_items=[], total="0.00")

    cart_items = cart.cart_items
    total = sum(float(item.plant.price) * item.quantity for item in cart_items)

    return render_template(
        "view_cart.html",
        cart_items=cart_items,
        total=f"{total:.2f}"
    )


# Updates the plant inventory and removes the cart items at checkout.
def apply_cart_at_checkout(cart):
    for item in cart.cart_items:
        item.plant.quantity -= item.quantity

    for item in cart.cart_items:
        db.session.delete(item)

    cart.status = CartStatus.INACTIVE


def create_order_obj(cart):
    cart_items = cart.cart_items

    order = Order(
        order_date=datetime.now(pytz.timezone('America/Denver')),
        order_total_item_amount=(
            sum(item.quantity for item in cart_items)
        ),
        order_cost=(
            sum(item.quantity * item.plant.price for item in cart_items)
        ),
        customer_id=current_user.id
    )

    db.session.add(order)
    db.session.flush()

    return order


def create_order_items_obj(order, cart):
    cart_items = cart.cart_items

    for cart_item in cart_items:
        order_item = OrderItem(
            quantity=cart_item.quantity,
            order=order,
            plant=cart_item.plant
        )
        db.session.add(order_item)


@app.route('/cart/order', methods=['POST'])
@login_required
@role_required('customer')
def order_submit():
    cart = get_or_create_cart(current_user)
    try:
        order = create_order_obj(cart)
        create_order_items_obj(order, cart)
        apply_cart_at_checkout(cart)

        db.session.commit()

        flash("Order successful!", "Success")
        return redirect(url_for('customer_dashboard'))

    except SQL_Execution_Error:
        db.session.rollback()

        flash("Error processing your order.", "Error")
        return redirect(url_for('error_page'))


def get_orders(customer_id: int):
    return (
        Order.query.filter_by(customer_id=customer_id)
        .order_by(Order.order_date.asc())
        .all()
    )


def get_order_items(order_id: int):
    return (
        OrderItem.query.filter_by(order_id=order_id)
        .order_by(OrderItem.quantity.asc())
        .all()
    )


@app.route('/myorders', methods=['GET'])
@login_required
@role_required('customer')
def view_orders():
    orders = get_orders(current_user.id)
    return render_template('view_orders.html', orders=orders)


@app.route('/myorders/<int:order_id>/invoice', methods=['GET'])
@login_required
@role_required('customer')
def view_items_in_order():
    return None


@app.route('/mydashboard', methods=['GET', 'POST'])
@login_required
@role_required('horticulturist')
def seller_dashboard():
    seller_listings = get_plants_by_seller(current_user.id)
    all_listings = get_all_plant_listings()
    return render_template(
        'seller_dashboard.html',
        seller_listings=seller_listings,
        all_listings=all_listings
    )


# Create a new plant listing for the logged-in horticulturist.
@app.route('/createplant', methods=['GET', 'POST'])
@login_required
@role_required('horticulturist')
def create_plant():
    form = PlantForm()
    if form.validate_on_submit():
        try:
            plant = Plant(
                name=form.name.data,
                color=form.color.data,
                variety=form.variety.data,
                climate=form.climate.data,
                quantity=form.quantity.data,
                price=form.price.data,
                seller_id=current_user.id
            )

            db.session.add(plant)
            db.session.commit()

            flash("Plant listing created.", "Success")
            return redirect(url_for('seller_dashboard'))

        except SQL_Execution_Error:
            db.session.rollback()

            flash("Error creating plant listing.", "Error")
            return redirect(url_for('error_page'))

    return render_template('create_plant.html', form=form)


@app.route('/updateplant/<int:plant_id>', methods=['GET', 'POST'])
@login_required
@role_required('horticulturist')
def update_plant(plant_id):
    form = PlantForm()
    plant = Plant.query.get_or_404(plant_id)

    if not form.is_submitted():
        form.process(obj=plant)

    if form.validate_on_submit():
        try:
            form.populate_obj(plant)
            db.session.commit()

            flash('Plant listing updated successfully.', 'Success')
            return redirect(url_for('seller_dashboard'))

        except SQL_Execution_Error:
            db.session.rollback()
            return redirect(url_for('error_page'))
    return render_template('update_plant.html', plant=plant, form=form,)


@app.route('/error', methods=['GET'])
def error_page():
    return render_template('error.html')
