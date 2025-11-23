'''
CSC3020
Description:
Notes:
'''


from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

import bcrypt

from app import app, db
from app.models import User, Plant
from app.forms import SignUpForm, LoginForm, PlantForm
from app.auth import role_required

# ===========================
# SIGN UP
# ===========================


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data != form.password_confirmation.data:
            flash("Incorrect Password!", "Error")
            return redirect(url_for('signup'))
        try:
            raw_password = form.password.data.encode()
            hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
            user = User(
                name=form.name.data,
                email=form.email.data.strip().lower(),
                password=hashed_password,
                role=form.role.data
                )

            db.session.add(user)
            db.session.commit()

            flash("Account created", "Success")
            return redirect(url_for('login'))

        except Exception:
            db.session.rollback()
            flash("Something Went Wrong Creating Your Account", "Error")
            return redirect(Url_for('display_error'))

    return render_template('signup.html', form=form)

# ===========================
# LOGIN
# ===========================


@app.route('/login', methods=['GET', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            login_user(user)

            if user.role == 'horticulturist':
                return redirect(Url_for('seller_dashboard'))
            return redirect(url_for('customer_dashboard'))
        else:
            flash("Invalid email or password", "Error")

    return render_template('login.html', form=form)

# ===========================
# LOGOUT
# ===========================


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Successfully logged out", "Success")
    return redirect(url_for('login'))

# ===========================
# CREATE PLANT (HORTICULTURIST ONLY)
# ===========================


@app.route('/plants/create', methods=['GET', 'POST'])
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
                price=float(form.price.data)
                )

            db.session.add(plant)
            db.session.commit()

            flash("Plant Listing Created", "Success")
            return redirect(url_for('display_error'))

        except Exception:
            db.session.rollback()

            flash("Error Creating Plant Listing", "Error")
            return redirect(url_for('display_error'))

    return render_template('create_plant.html', form=form)
