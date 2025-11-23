"""
Author: Mckenna
Description:
"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app import models
from app.models import User
import os
from app import routes

app = Flask('Unbeleafable App')
app.secret_key = 'green thumbs'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

loginManager = LoginManager()
loginManager.init_app(app)


@loginManager.user_loader
def load_user(id):
    try:
        return db.session.query(User).filter(User.id == id).one()
    except Exception:
        return None
