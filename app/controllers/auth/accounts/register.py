# Flask
from flask import render_template, redirect, url_for
from flask import current_app
# Flask Extensions
from flask_login import current_user
# App Objects
from app import db, bcrypt
# App Models
from app.models.user import User
# Forms and Routes, others
from .forms import RegistrationForm
from . import bp


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(email=email,
                    password=hashed_password, 
                    first_name=first_name, 
                    last_name=last_name, 
                    active=True)
        if user.verify_existing(email=email):
            db.session.add(user)
            db.session.commit()
            print("Usuário registrado com sucesso.")
        else:
            print("Usuário não pôde ser registrado.")


        return redirect(url_for('auth.login'))
    else:
        return render_template('auth/accounts/register.html', form=form)
