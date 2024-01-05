from flask import render_template, flash
from flask_login import login_required
from . import bp


@bp.route("/", methods=['GET', 'POST'])
@login_required
def home():
    # regra de negocio
    return render_template('home/inicio/index.html')