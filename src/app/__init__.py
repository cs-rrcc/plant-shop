"""
Author: Mckenna
Description: This file initializes the Flask application,
instantiates the required Flask objects, defines module
imports, and sets up the Flask application's configuration.
"""

from flask import Flask
import os

app = Flask('Unbeleafable App')
app.secret_key = 'green thumbs'


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plant_shop.db'
db = SQLAlchemy(app)


from app import models
with app.app_context():
    db.create_all()


from flask_login import LoginManager
loginManager = LoginManager()
loginManager.init_app(app)


from app.models import User
@loginManager.user_loader
def load_user(id):
    try:
        return db.session.query(User).filter(User.id == id).one()
    except Exception:
        return None

from app import routes
