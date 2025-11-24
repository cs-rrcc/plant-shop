"""
Author(s):
Description:
"""


from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, login_required, logout_user

import bcrypt

from app import app, db
from app.auth import role_required
from app.forms import LoginForm, PlantForm, SignUpForm
from app.models import Plant, User


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
    return Plant.query.all()


def get_plants_by_seller(id):
    return (
        Plant.query.filter_by(seller_id=id)
        .order_by(Plant.quantity.asc())
        .all()
    )


def get_plants_by_category(category):
    pass


@app.route('/buydashboard', methods=['GET', 'POST'])
@login_required
@role_required('customer')
def customer_dashboard():
    return render_template('customer_dashboard.html')


@app.route('/listdashboard', methods=['GET', 'POST'])
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
