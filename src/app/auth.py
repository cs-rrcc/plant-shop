'''
CSC3020
Author: Mckenna
Notes: A small, custom wrapper to enforce user authentication between the two roles in the user model.
'''

from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            allowed_role = role
            user_role = current_user.role.lower() #incase url is directly accessed and passes in role
            if user_role != allowed_role:
                return redirect(url_for('display_error'))
            return f(*args, **kwargs)
        return decorator
    return wrapper