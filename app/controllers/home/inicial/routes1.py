from flask import render_template
from . import bp


@bp.route('/homepage', methods=['GET', 'POST'])
def rotaum():
    # regra de negocio
    return render_template('home/inicio/index.html')