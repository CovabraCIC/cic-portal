from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = EmailField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
    submit = SubmitField()

class ForgotForm(FlaskForm):
    email = EmailField(validators=[validators.DataRequired()])
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    first_name = StringField(validators=[validators.DataRequired()])
    last_name = StringField(validators=[validators.DataRequired()])
    email = EmailField(validators=[validators.DataRequired()])
    password = PasswordField('Senha', validators=[validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirmar Senha', validators=[validators.DataRequired(), validators.Length(min=6, max=10)])
    submit = SubmitField()