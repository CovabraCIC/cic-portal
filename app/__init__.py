from flask import Flask, g
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from database import db
from config import ProductionConfig
from app.models.user_role import UserRoles
from app.models.role import Role
from app.models.user import User


# Extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
admin = Admin(name="Controle CIC", template_mode="bootstrap3")

# Config Extensions
class UserView(ModelView):
    column_list = ['id', 'first_name', 'roles']
    form_excluded_columns = ['roles']

admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Role, db.session))

def create_app():
    app = Flask(__name__, template_folder="views", static_folder="public")
    app.config.from_object(ProductionConfig)
    
    # Import blueprints
    from .controllers.home.inicial import bp as home_bp
    from .controllers.auth.accounts import bp as auth_bp
    from .controllers.errors.exemplares import bp as errors_bp
    from .controllers.financeiro.exemplares import bp as financeiro_bp
    from .controllers.comercial.solicitacao_devolucoes import bp as solicitacao_devolucoes_bp

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(financeiro_bp)
    app.register_blueprint(solicitacao_devolucoes_bp)

    # Extensions Init
    db.init_app(app=app)
    login_manager.init_app(app=app)
    bcrypt.init_app(app=app)
    admin.init_app(app=app)

    with app.app_context(): #! It is important that you import your models after initializing the db object since.
        db.create_all()

    return app
