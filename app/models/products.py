from database import db
"""Example users model"""

class Product(db.Model):
    __tablename__ = 'products'
    __bind_key__ = 'QAS'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    local = db.Column(db.String(32), nullable=False)

    def __init__(self, nome, descricao, local):
        self.nome = nome
        self.descricao = descricao
        self.local = local
        
    def save(self):
        """save in the database"""

        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        """delete from database"""

        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % self.nome