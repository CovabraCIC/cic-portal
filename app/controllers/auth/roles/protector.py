from flask import abort, flash
from flask_login import current_user
from functools import wraps


def role_required(required_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                roles = [user_role.roles.name for user_role in current_user.roles]
                if any(role in roles for role in required_roles):
                    return func(*args, **kwargs)
                else:
                    flash('Você não tem permissão para acessar esta página.', "danger")
                    return abort(403)
            else:
                flash('Você não tem permissão para acessar esta página.', "danger")
                return abort(403)
        return wrapper
    return decorator