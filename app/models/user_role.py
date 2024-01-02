from database import db


class UserRoles(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=1)

    user = db.relationship('User', backref=db.backref('user_role', cascade='all, delete-orphan'))
    role = db.relationship('Role', backref=db.backref('user_role', cascade='all, delete-orphan'))