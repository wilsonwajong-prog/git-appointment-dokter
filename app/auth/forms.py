from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    example = RadioField('UserType', choices=[('val1', 'Docter'), ('val2', 'Pasien')])
    rememberme = BooleanField('remember me')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(1, 20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_passwword = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])
    example = RadioField('UserType', choices=[('val1', 'Docter'), ('val2', 'Pasien')])
    submit = SubmitField("Register")


