from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, Email, DataRequired, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = IntegerField("Phone number", validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
   