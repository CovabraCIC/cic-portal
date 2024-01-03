from . import bp
from flask import render_template


# 404 Page not found error default handler
@bp.app_errorhandler(404)
def handle404(error):
    return render_template('errors/exemplares/404.html')

# 403 Forbidden
@bp.app_errorhandler(403)
def handle404(error):
    return render_template('errors/exemplares/403.html')