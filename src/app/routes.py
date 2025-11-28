"""
Author(s):
Description:
"""


from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

import bcrypt

from app import app, db
from app.auth import role_required
from app.forms import CategoryViewForm, LoginForm, PlantForm, SignUpForm
from app.models import Plant, User, Cart, CartItem


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
                role=form.role.data
                )

            db.session.add(user)
            db.session.commit()

            flash("Account created", "Success")
            return redirect(url_for('login'))

        except Exception:
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

            if user.role == 'horticulturist':
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


def get_plants_by_seller(id):
    return (
        Plant.query.filter_by(seller_id=id)
        .order_by(Plant.quantity.asc())
        .filter(Plant.quantity > 0)
        .all()
    )


def get_plants_by_category(variety, climate):
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
        except Exception as e:
            print(e)
            return redirect(url_for('error_page'))

    return render_template(
        'customer_dashboard.html',
        listings=listings,
        form=form
    )

@app.route('/cart/add', methods=['POST'])
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
    cart = current_user.cart
    if cart is None:
        cart = Cart(customer=current_user, status="ACTIVE")
        db.session.add(cart)
        db.session.flush()  # ensure cart.id exists

    # See if this plant is already in the cart
    cart_item = CartItem.query.filter_by(
        cart_id=cart.id,
        plant_id=plant.id
    ).first()

    if cart_item:
        new_qty = cart_item.quantity + quantity

        # Make sure the total in cart does not exceed stock
        if new_qty > plant.quantity:
            remaining = plant.quantity - cart_item.quantity
            if remaining <= 0:
                flash(
                    "You already have the maximum available quantity of this plant in your cart.",
                    "Error"
                )
            else:
                flash(
                    f"You can only add {remaining} more of this plant.",
                    "Error"
                )
            return redirect(url_for("customer_dashboard"))

        cart_item.quantity = new_qty
    else:
        cart_item = CartItem(
            cart=cart,
            plant=plant,
            quantity=quantity
        )
        db.session.add(cart_item)

    db.session.commit()
    flash(f"Added {quantity} × {plant.name} to your cart.", "Success")
    return redirect(url_for("customer_dashboard"))


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

            flash("Plant Listing Created", "Success")
            return redirect(url_for('seller_dashboard'))

        except Exception:
            db.session.rollback()

            flash("Error Creating Plant Listing", "Error")
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

            return redirect(url_for('seller_dashboard'))

        except Exception:
            db.session.rollback()
            return redirect(url_for('error_page'))
    return render_template('update_plant.html', plant=plant, form=form,)


@app.route('/error', methods=['GET'])
def error_page():
    return render_template('error.html')
