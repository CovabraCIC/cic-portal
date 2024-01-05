from flask import Blueprint

bp = Blueprint('comercial', __name__, url_prefix="/comercial")

from .routes import formulario_solicitacao_devolucoes, solicitacao_devolucoes