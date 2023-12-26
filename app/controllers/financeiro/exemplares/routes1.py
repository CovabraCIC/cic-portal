# Flask
from flask import render_template
# Flask Extensions
from flask_login import login_required
# App Objects
from app import db
# App Models
from app.models.products import Product
# Forms and Routes, others
from . import bp
from sqlalchemy import text


@bp.route('/rota1', methods=['GET', 'POST'])
@login_required
def lista_produtos():
    # regra de negocio
    # query = text("SELECT * FROM products")
    # result = db.session.execute(query, bind_arguments={"mapper": Product})
    # db.session.commit() # Não é necessário, apenas para demonstração de commit.
    # return render_template('financeiro/exemplares/list_products.html', products=result)
    return "random text"
