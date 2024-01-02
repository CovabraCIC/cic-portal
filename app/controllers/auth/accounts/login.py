# Flask
from flask import render_template, redirect, url_for
from flask import current_app, flash
# Flask Extensions
from flask_login import login_user, login_required, logout_user, current_user
# App Objects
from app import login_manager, bcrypt
# App Models
from app.models.user import User
# Forms and Routes, others
from .forms import LoginForm
from . import bp


login_manager.login_view = 'auth.login' # Redirecionar usuários não autenticados para esta rota.

@login_manager.user_loader
def load_user(user_id):
    """Define como o Flask-Login carrega um usuário com base no ID armazenado no cookie de sessão.
    Internamente utilizado para carregar o objeto do usuário após autenticação, em todas as solicitações subsequentes."""
    return User.query.get(int(user_id))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Usuário logado com sucesso.", "success")
            return redirect(url_for('auth.home'))
        else:
            flash("Inconsistencia no ato do login.", "danger")
    return render_template('auth/accounts/login.html', form=form)


@bp.route("/logout")
@login_required
def logout():
    """Encerra a sessão do usuário autenticado, gerando um cookie armazenado no navegador do cliente."""
    logout_user() 
    return redirect(url_for('auth.login'))


@bp.route("/home")
@login_required
def home():
    """Página de exemplo com login requerido para demonstração."""
    return render_template('home/inicio/index.html', current_user=current_user)