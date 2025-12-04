"""
Author: Mckenna
Description: A customer wrapper class that confirms
if the user has the required role to access a route.
"""

from functools import wraps
from flask_login import current_user
from flask import redirect, url_for


def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            allowed_role = role
            user_role = current_user.role.value
            if user_role != allowed_role:
                return redirect(url_for('error_page'))
            return f(*args, **kwargs)
        return decorator
    return wrapper
