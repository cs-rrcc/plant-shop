'''
CSC3020
Description: models for CTF project
Notes: Contains User, Competition, and Challenge models.
'''

from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    role = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
