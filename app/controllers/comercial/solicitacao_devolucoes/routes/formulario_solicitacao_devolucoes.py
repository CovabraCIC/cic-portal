from flask import render_template, request, redirect, url_for, flash
from ..utils.forms import MeuFormulario
from app.models.comercial.solicitacao_devolucoes.solicitacoes import TipoSolicitacaoDevolucaoCd, SolicitacaoDevolucaoCd, list_estab, dict_products
from .. import bp
from flask_login import login_required
from app.controllers.auth.roles.protector import role_required


@bp.route("/formulario_solicitacao/<id>", methods=['GET', 'POST'])
@login_required
@role_required(["comercial", "user"])
def formulario_solicitacao(id):

    list_tipos = [ ( str(tipo.id), tipo.tipo ) for tipo in TipoSolicitacaoDevolucaoCd.query.all() ] 

    estabelecimentos = list_estab()
    produtos = dict_products()

    form = MeuFormulario()
    form.tipodevolucao.choices = list_tipos
    form.estabelecimento.choices = estabelecimentos

    form_title = 'Nova Solicitação de Devolução'
    form_subtitle = None

    if id != '0':

        solicitacao = SolicitacaoDevolucaoCd.get_by_id(id=id)

        if solicitacao != None and solicitacao.idstatussolicitacaodevolucaocd == 1:
            form.fill(solicitacao)
            form_title = 'Editar Solicitação de Devolução'
            form_subtitle = f'loja {solicitacao.idestabelecimento} e produto {solicitacao.idproduto}'
        else: 
            flash('SOLICITAÇÃO NÃO PODE SER ALTERADA! Solicitacão já em andamento.', 'danger')
            return redirect( url_for('comercial.solicitacoes_devolucoes') )
    

    if form.is_submitted():
        result = request.form.to_dict(flat=False)

        produto = [ produto for produto in produtos if produto['id'] == int(result.get('idproduto')[0]) ]

        if len(produto) > 0:
            if not SolicitacaoDevolucaoCd.verify_exists_another(id, result.get('estabelecimento')[0], result.get('idproduto')[0]):
                if id == '0':
                    SolicitacaoDevolucaoCd.create(result)
                    flash('SOLICITAÇÃO REGISTRADA COM SUCESSO!', 'success')
                    return redirect( url_for('comercial.solicitacoes_devolucoes') )
                else:
                    SolicitacaoDevolucaoCd.update(result, id)
                    flash('SOLICITAÇÃO ALTERADA COM SUCESSO!', 'success')
                    return redirect( url_for('comercial.solicitacoes_devolucoes') )
            else:
                flash('SOLICITAÇÃO NEGADA! Solicitação na mesma loja para o mesmo produto inda em andamento', 'danger')
        else: flash('SOLICITAÇÃO NEGADA! Produto Invalido', 'danger')

                
    return render_template('comercial/solictacao_devolucoes/forms.html', form=form, lista_produtos=produtos, form_title=form_title, form_subtitle=form_subtitle)

