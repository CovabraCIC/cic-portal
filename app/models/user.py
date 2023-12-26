from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary="roles_users",
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email


    def __init__(self, name, email, password, active):
        self.name = name
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

    def verify_existing(self, session, **primary_keys:dict) -> bool:
        """Retorna True se a consulta existir."""
        existing_item = session.query(self.__class__).filter_by(**primary_keys).first()
        return existing_item is None

    def __repr__(self):
        return '<User %r>' % self.name
    
    def __str__(self):
        return self.name