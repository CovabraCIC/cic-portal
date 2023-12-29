# Flask Home
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
# Flask Basement
from flask_admin.contrib.sqla import ModelView
# Flask Config
from config import DevelopmentConfig
# Models
from app.models.role_user import roles_users
from app.models.role import Role
from app.models.user import User
# App Objects
from database import db


# Extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
admin = Admin(name="Controle CIC", template_mode="bootstrap3")

# Config Extensions
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))

def create_app():
    app = Flask(__name__,
                template_folder="views",
                static_folder="public"
                )
    
    app.config.from_object(DevelopmentConfig)
    
    # Import blueprints
    from .controllers.home.inicial import bp as home_bp
    from .controllers.auth.accounts import bp as auth_bp
    from .controllers.errors.exemplares import bp as errors_bp
    from .controllers.financeiro.exemplares import bp as financeiro_bp

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(financeiro_bp)

    # # DB / Extensions
    db.init_app(app=app)
    login_manager.init_app(app=app)
    bcrypt.init_app(app=app)
    admin.init_app(app=app)

    with app.app_context(): #! It is important that you import your models after initializing the db object since.
        db.create_all()

    return app
