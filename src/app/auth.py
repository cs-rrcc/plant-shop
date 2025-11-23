"""
Author: Mckenna
Description:
"""

from functools import wraps
from flask_login import current_user
from flask import redirect, url_for


def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            allowed_role = role
            user_role = current_user.role.lower()
            if user_role != allowed_role:
                return redirect(url_for('display_error'))
            return f(*args, **kwargs)
        return decorator
    return wrapper
