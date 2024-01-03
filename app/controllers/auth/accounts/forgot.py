from . import bp
from flask import render_template, redirect, url_for, flash, request
from .forms import ForgotForm
from app import db, bcrypt
from app.utils import flash_form_errors
from app.models.user import User


@bp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotForm()

    if request.method == 'POST' and form.validate():
        email = form.data['email']
        
        if not User.verify_existing(email=email):
            flash("Usuário registrado com sucesso.", "success")
            return redirect(url_for('auth.forgot'))
        #     except Exception as e:
        #         db.session.rollback()
        #         flash("Tente novamente, erro no banco de dados", "warning")
        #         return render_template('auth/accounts/register.html', form=form)
        else:
            flash("Inconsistência no ato do registro, verifique os dados.", "danger")
    else:
        flash_form_errors(form)
    return render_template('auth/accounts/forgot.html', form=form)
