from flask import Blueprint


bp = Blueprint('financeiro', __name__, url_prefix="/finance")
from . import routes1, routes2