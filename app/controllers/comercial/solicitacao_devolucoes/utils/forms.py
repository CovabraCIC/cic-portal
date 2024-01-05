from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField, TextAreaField
from wtforms.validators import DataRequired


class MeuFormulario(FlaskForm):

    estabelecimento = SelectField('Estabelecimento', validators=[DataRequired()])
    idproduto = IntegerField('Id do Produto', validators=[DataRequired()])
    quantidade = DecimalField('Quantidade', validators=[DataRequired()])
    tipodevolucao = SelectField('Tipo de Devolução')
    observacoes = TextAreaField('OBS.:')

    enviar = SubmitField('Enviar')

    def fill(self, solicitacao):
        self.estabelecimento.data = str(solicitacao.idestabelecimento)
        self.idproduto.data = solicitacao.idproduto
        self.quantidade.data = solicitacao.quantidade
        self.tipodevolucao.data = solicitacao.idtiposolicitacaodevolucaocd
        self.observacoes.data = solicitacao.observacao
