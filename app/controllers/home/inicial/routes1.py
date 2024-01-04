from flask import render_template
from flask_login import login_required, current_user
from . import bp


@bp.route("/", methods=['GET', 'POST'])
@login_required
def home():
    # regra de negocio
    return render_template('home/inicio/index.html', current_user=current_user)