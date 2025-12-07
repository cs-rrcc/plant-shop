"""
Author: Mckenna
Description: The classes defined in this file
create the application's objects and their relationships
These objects include the user, plant, cart, cart items,
order, order items, and several enums and data constraints.
"""

from flask_login import UserMixin
from enum import Enum as py_enum
from sqlalchemy import Enum as SQL_enum
from sqlalchemy.orm import validates
from app import db


class UserRole(py_enum):
    HORTICULTURIST = "horticulturist"
    CUSTOMER = "customer"


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)

    plants_for_sale = db.relationship(
        'Plant',
        back_populates='horticulturist',
        lazy=True,
        cascade='all, delete-orphan'
    )

    cart = db.relationship(
        'Cart',
        back_populates='customer',
        uselist=False,
        cascade='all, delete-orphan',
        lazy=True
    )

    orders = db.relationship(
        'Order',
        back_populates='customer',
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
    price = db.Column(db.Numeric(15, 2), nullable=False, default=0.00)
    seller_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    horticulturist = db.relationship(
        "User",
        back_populates='plants_for_sale'
    )

    cart_items = db.relationship(
        'CartItem',
        back_populates='plant',
        lazy=True
    )

    order_items = db.relationship(
        'OrderItem',
        back_populates='plant',
        lazy=True
    )

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        if quantity < 0:
            raise ValueError('Quantity cannot be less than zero')
        return quantity

    @validates('price')
    def validate_price(self, key, price):
        if price < 0:
            raise ValueError('Price cannot be less than zero')
        return price

    def __repr__(self):
        return f'<Plant {self.name}>'


class CartStatus(py_enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(
        db.Enum(CartStatus),
        nullable=False,
        default=CartStatus.ACTIVE
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    customer = db.relationship(
        'User',
        back_populates='cart'
    )

    cart_items = db.relationship(
        'CartItem',
        back_populates='cart',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Cart {self.id}>'


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    plant_id = db.Column(
        db.Integer,
        db.ForeignKey('plants.id'),
        nullable=False
    )

    cart_id = db.Column(
        db.Integer,
        db.ForeignKey('carts.id'),
        nullable=False
    )

    plant = db.relationship('Plant', back_populates='cart_items')
    cart = db.relationship('Cart', back_populates='cart_items')

    def __repr__(self):
        return f'<Cart Item {self.id}>'


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    order_total_item_amount = db.Column(db.Integer, nullable=False)
    order_cost = db.Column(db.Numeric(15, 2), nullable=False, default=0.00)

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    customer = db.relationship(
        'User',
        back_populates='orders'
    )

    order_items = db.relationship(
        'OrderItem',
        back_populates='order',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Order {self.id}>'


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    order_id = db.Column(
        db.Integer,
        db.ForeignKey('orders.id'),
        nullable=False
    )

    plant_id = db.Column(
        db.Integer,
        db.ForeignKey('plants.id'),
        nullable=False
    )

    order = db.relationship('Order', back_populates='order_items')
    plant = db.relationship('Plant', back_populates='order_items')

    def __repr__(self):
        return f'<Order Item {self.id}>'
