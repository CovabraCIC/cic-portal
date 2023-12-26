from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
    email = EmailField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    name = StringField(validators=[validators.DataRequired()])
    email = EmailField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
    confirm_password = PasswordField(validators=[validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField()