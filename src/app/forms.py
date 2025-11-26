"""
Author(s):
Description:
"""

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired, DataRequired, NumberRange, Email


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )

    role = SelectField(
        'Role',
        choices=['horticulturist', 'customer'],
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PlantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])

    variety = SelectField(
        'Variety',
        choices=['tree', 'flower', 'shrub', 'herb'],
        validators=[DataRequired()]
    )

    climate = SelectField(
        'Climate Type',
        choices=['arid', 'cold', 'temperate', 'tropical'],
        validators=[DataRequired()]
    )

    quantity = IntegerField(
        'Quantity',
        validators=[InputRequired(), NumberRange(min=0)]
    )
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    submit = SubmitField('List')


class CategoryViewForm(FlaskForm):
    variety = SelectField(
        'Select Plant Variety',
        choices=['all', 'tree', 'flower', 'shrub', 'herb'],
        validators=[DataRequired()]
    )

    climate = SelectField(
        'Select Climate Type',
        choices=['all', 'arid', 'cold', 'temperate', 'tropical'],
        validators=[DataRequired()]
    )

    submit = SubmitField('Browse')
