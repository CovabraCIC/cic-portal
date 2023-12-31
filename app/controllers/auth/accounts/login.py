from . import bp
from flask import render_template, redirect, url_for, flash, session, g
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm
from app import login_manager, bcrypt
from app.models.user import User


login_manager.login_view = "auth.login"
login_manager.login_message = "Você precisa estar logado para visualizar essa página."
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    """Define como o Flask-Login carrega um usuário com base no ID armazenado no cookie de sessão.
    Internamente utilizado para carregar o objeto do usuário após autenticação, em todas as solicitações subsequentes."""
    # if session["user_id"]:
    #     user = User.query.filter_by(id=session["user_id"]).first()
    # else:
    #     user = {"name": "Guest"}  # Make it better, use an anonymous User instead
    # g.user = user

    return User.query.get(int(user_id))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.data["email"]
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, form.data["password"]):
            login_user(user)
            session['logged_in'] = True
            session['user_id'] = user.id
            flash("Usuário logado com sucesso.", "success")
            return redirect(url_for('home.home'))
        else:
            flash("Inconsistência no ato do login.", "danger")
    return render_template('auth/accounts/login.html', form=form)

@bp.route("/logout")
@login_required
def logout():
    if session.get('logged_in'):
        session.pop('logged_in', None)
        logout_user()
        flash('Usuário deslogado com sucesso.', "success")
    else:
        flash("Você não está logado.", "danger")
    return redirect(url_for('auth.login'))