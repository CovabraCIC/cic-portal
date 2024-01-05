from datetime import datetime, timedelta
from sqlalchemy import text, or_, desc
from database import db

class TipoSolicitacaoDevolucaoCd(db.Model):
    __tablename__ = 'tiposolicitacaodevolucaocd'
    #__bind_keys__ = 'cic'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String())
    descricao = db.Column(db.String())


class StatusSolicitacaoDevolucaoCd(db.Model):
    __tablename__ = 'statussolicitacaodevolucaocd'
    #__bind_keys__ = 'cic'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())
    descricao = db.Column(db.String())


class SolicitacaoDevolucaoCdProduto(db.Model):
    __tablename__ = 'solicitacaodevolucaocdproduto'
    #__bind_keys__ = 'cic'
    id = db.Column(db.Integer, primary_key=True)
    descricaoproduto = db.Column(db.String())
    setorproduto = db.Column(db.String())


class SolicitacaoDevolucaoCd(db.Model):
    __tablename__ = 'solicitacaodevolucaocd'
    #__bind_keys__ = 'cic'
    id = db.Column(db.Integer, primary_key=True)
    idestabelecimento = db.Column(db.Integer)
    idproduto = db.Column(db.Integer)
    quantidade = db.Column(db.Float)
    idtiposolicitacaodevolucaocd = db.Column(db.Integer)
    observacao = db.Column(db.String())
    datahoracriacao = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    idstatussolicitacaodevolucaocd = db.Column(db.Integer)
    datahoraalteracao = db.Column(db.DateTime(timezone=True))

    def __init__(self, idestabelecimento, idproduto, quantidade, idtiposolicitacaodevolucaocd,
                        observacao, idstatussolicitacaodevolucaocd):
        self.idestabelecimento = idestabelecimento,
        self.idproduto = idproduto,
        self.quantidade = quantidade,
        self.idtiposolicitacaodevolucaocd = idtiposolicitacaodevolucaocd,
        self.observacao = observacao,
        self.idstatussolicitacaodevolucaocd = idstatussolicitacaodevolucaocd


    @classmethod
    def verify_exists_another(cls, id, idestabelecimento, idproduto):
        solicitacoes_andamento = cls\
                                    .query\
                                    .filter(cls.idestabelecimento==idestabelecimento,
                                                cls.idproduto==idproduto,
                                                cls.idstatussolicitacaodevolucaocd<=3,
                                                cls.id!=id)\
                                    .count()
        
        return solicitacoes_andamento != 0

    @classmethod
    def create(cls, result: dict):

        solicitacao = cls(idestabelecimento = int(result.get('estabelecimento')[0]),
                        idproduto = result.get('idproduto')[0],
                        quantidade = result.get('quantidade')[0],
                        idtiposolicitacaodevolucaocd = int(result.get('tipodevolucao')[0]),
                        observacao = result.get('observacoes')[0],
                        idstatussolicitacaodevolucaocd = 1)
        
        db.session.add(solicitacao)
        db.session.commit()

    @classmethod
    def update(cls, result: dict, id: int):
        solicitacao = cls.query.filter(cls.id==id).first()

        solicitacao.idestabelecimento = int(result.get('estabelecimento')[0])
        solicitacao.idproduto = result.get('idproduto')[0]
        solicitacao.quantidade = result.get('quantidade')[0]
        solicitacao.idtiposolicitacaodevolucaocd = int(result.get('tipodevolucao')[0])
        solicitacao.observacao = result.get('observacoes')[0]
        solicitacao.idstatussolicitacaodevolucaocd = 1
        
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.id==id).first()
    
    @classmethod
    def get_solicitacoes(cls):

        data_limite = datetime.utcnow() - timedelta(days=4)

        return db.session\
            .query(cls, TipoSolicitacaoDevolucaoCd, StatusSolicitacaoDevolucaoCd, SolicitacaoDevolucaoCdProduto)\
                .join(TipoSolicitacaoDevolucaoCd, 
                    cls.idtiposolicitacaodevolucaocd == TipoSolicitacaoDevolucaoCd.id)\
                .join(StatusSolicitacaoDevolucaoCd,
                      cls.idstatussolicitacaodevolucaocd == StatusSolicitacaoDevolucaoCd.id)\
                .join(SolicitacaoDevolucaoCdProduto,
                      cls.idproduto == SolicitacaoDevolucaoCdProduto.id)\
                .filter(or_(
                            cls.idstatussolicitacaodevolucaocd < 6,
                            cls.datahoraalteracao <= data_limite
                            ))\
                    .order_by(desc(cls.datahoracriacao))\
                        .all()


def list_estab():
    sql_lojas = text("SELECT id FROM dblink('dbname=erp', 'SELECT id FROM estabelecimento WHERE comercialmenteativo = ''S'' AND id < 95') e (id int) ORDER BY 1")
    lojas = db.session.execute(sql_lojas)
    return [ (str(e[0]), f'Loja {e[0]}') for e in lojas ]

def dict_products():
    sql_produtos = text("SELECT id, codigobarras, descricaoproduto FROM dblink('dbname=erp', 'SELECT id, codigobarras, descricaoproduto FROM produto WHERE exclusivoecommerce = ''N'' and codigobarras IS NOT NULL ') e (id int, codigobarras text, descricaoproduto text) ORDER BY 1")
    produtos = db.session.execute(sql_produtos).all()
    return [ {"id":p[0], "codigobarras":p[1], "descricao":p[2].replace("'","").replace('"',"") } for p in produtos ]

