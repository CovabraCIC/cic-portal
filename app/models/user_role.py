from database import db


class UserRoles(db.Model):
    __tablename__ = 'user_role'
    __table_args__ = {"schema":"portal"}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('portal.user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('portal.role.id'), nullable=False, default=1)

    users = db.relationship('User', back_populates='roles')
    roles = db.relationship('Role', back_populates='users')

    def __str__(self):
        return self.roles.name