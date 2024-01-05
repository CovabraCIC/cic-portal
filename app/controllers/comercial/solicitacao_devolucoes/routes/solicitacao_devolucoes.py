from flask import render_template
from app.models.comercial.solicitacao_devolucoes.solicitacoes import SolicitacaoDevolucaoCd
from .. import bp
from flask_login import login_required
from app.controllers.auth.roles.protector import role_required

@bp.route('/solicitacao_devolucoes')
@login_required
@role_required(["comercial", "user"])
def solicitacoes_devolucoes():
    
    solicitacoes = SolicitacaoDevolucaoCd.get_solicitacoes()

    return render_template('comercial/solictacao_devolucoes/solicitacoes_devolucoes.html', solicitacoes=solicitacoes)
