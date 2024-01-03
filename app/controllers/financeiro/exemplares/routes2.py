from . import bp
from flask import render_template
from app import db
from app.models.user import User


@bp.route('/rota2', methods=['GET', 'POST'])
def lista_usuarios():
    # regra de negocio
    # uzuarios = User.query.all()
    # db.session.commit() # Não é necessário, apenas para demonstração de commit.
    # return render_template('financeiro/exemplares/list_users.html', users=uzuarios)
    return "random text"