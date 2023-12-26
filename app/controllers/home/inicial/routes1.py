# Flask
from flask import render_template
# Forms and Routes, others
from . import bp

@bp.route('/homepage', methods=['GET', 'POST'])
def rotaum():
    # regra de negocio
    return render_template('home/inicio/index.html')
