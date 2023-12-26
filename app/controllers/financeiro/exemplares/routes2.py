# Flask
from flask import render_template
# App Objects
from app import db
# App Models
from app.models.user import User
# Forms and Routes, others
from . import bp


@bp.route('/rota2', methods=['GET', 'POST'])
def lista_usuarios():
    # regra de negocio
    # uzuarios = User.query.all()
    # db.session.commit() # Não é necessário, apenas para demonstração de commit.
    # return render_template('financeiro/exemplares/list_users.html', users=uzuarios)
    return "random text"