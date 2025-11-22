'''
CSC3020
Authors:
Notes:
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

    plant_seller = db.relationship(
        'Plant',
        backref='horticulturist',
        lazy=True
    )

    def __repr__(self):
        return f'<User {self.email}>'


class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    color = db.Column(db.String(35), nullable=False)
    variety = db.Column(db.String(10), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Double, nullable=False, default=0.00)

    def __repr__(self):
        return f'<Plant {self.name}>'
