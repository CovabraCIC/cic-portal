from functools import wraps
from flask import abort, flash
from flask_login import current_user

def role_required(required_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                roles = [user_role.role.name for user_role in current_user.user_role]
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