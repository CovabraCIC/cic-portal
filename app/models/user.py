from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {"schema":"portal"}
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('UserRoles', back_populates='users')

    def __str__(self):
        return self.email


    def __init__(self, first_name, last_name, email, password, active):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.active = active

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    @classmethod
    def verify_existing(cls, **primary_keys:dict) -> bool:
        """Retorna True se a consulta existir."""
        existing_item = db.session.query(cls).filter_by(**primary_keys).first()
        return existing_item is not None

    def __repr__(self):
        return '<User %r>' % self.first_name
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name