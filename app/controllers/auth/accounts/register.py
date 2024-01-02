from . import bp
from .forms import RegistrationForm
# Flask
from flask import render_template, redirect, url_for, flash, request
# App
from app import db, bcrypt
from app.utils import flash_form_errors
from app.models.user_role import UserRoles
from app.models.user import User
from app.models.role import Role

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        first_name = form.data['first_name']
        last_name = form.data['last_name']
        email = form.data['email']
        hashed_password = bcrypt.generate_password_hash(form.data['password']).decode('utf-8')

        
        if not User.verify_existing(email=email):
            try:
                user = User(email=email, password=hashed_password, first_name=first_name, last_name=last_name, active=True)
                db.session.add(user)
                db.session.flush() # Importante para que o ID do usuário seja coletado.
                user_roles = UserRoles(user_id=user.id)
                db.session.add(user_roles)
                db.session.commit()
                flash("Usuário registrado com sucesso.", "success")
                return redirect(url_for('auth.login'))
            except Exception as e:
                db.session.rollback()
                flash("Tente novamente, erro no banco de dados", "warning")
                return render_template('auth/accounts/register.html', form=form)
        else:
            flash("Inconsistência no ato do registro, verifique os dados.", "danger")
    else:
        flash_form_errors(form)
    return render_template('auth/accounts/register.html', form=form)
