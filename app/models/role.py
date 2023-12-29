from database import db


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def verify_existing(self, **primary_keys:dict) -> bool:
        """Retorna True se a consulta existir."""
        existing_item = db.session.query(self.__class__).filter_by(**primary_keys).first()
        return existing_item is None

    def __repr__(self):
        return '<Role %r>' % self.name
    
    def __str__(self):
        return self.name, "-", self.description