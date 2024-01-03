from . import bp
from flask import render_template
from flask_login import login_required
from app import db
from app.models.products import Product
from app.controllers.auth.roles.protector import role_required
from sqlalchemy import text


@bp.route('/rota1', methods=['GET', 'POST'])
@login_required
@role_required(["fiscal", "user"])
def lista_produtos():
    # regra de negocio
    # query = text("SELECT * FROM products")
    # result = db.session.execute(query, bind_arguments={"mapper": Product})
    # db.session.commit() # Não é necessário, apenas para demonstração de commit.
    # return render_template('financeiro/exemplares/list_products.html', products=result)
    return "random text"
