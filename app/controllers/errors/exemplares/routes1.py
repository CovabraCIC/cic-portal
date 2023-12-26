# Flask
from flask import render_template
# Forms and Routes, others
from . import bp


# 404 Page not found error default handler
@bp.app_errorhandler(404)
def handle404(error):
    return render_template('errors/exemplares/404.html')