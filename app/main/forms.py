from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField
from flask_wtf import Form
from wtforms.fields.html5 import DateField

class ExampleForm(FlaskForm):
    dt = DateField("DatePicker", format="%Y-%m-%d")
    dokters = SelectField("Dokter", choices=[])
    submit = SubmitField('input')




class UpdateDocterAccount(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(1, 20)])

    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                        Email()])
    speciality = StringField("Speciality",
                             validators=[DataRequired(), Length(5, 60)])
    address = StringField("Address",
                             validators=[DataRequired(), Length(5, 60)])
    file_img = FileField('file')
    submit = SubmitField('Update')


class UpdatePatientAccount(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(1, 20)])

    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                        Email()])
    age = IntegerField("Umur", validators=[DataRequired()])
    gender = RadioField('UserType', choices=[('male', 'Pria'), ('female', 'Wanita')])
    address = StringField("Address",
                            validators=[DataRequired(), Length(5, 60)])
    file_img = FileField('file')
    submit = SubmitField('Update')

