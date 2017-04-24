from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm 

class LoginForm(FlaskForm):
    fullname = StringField('fullname', validators=[InputRequired(), Length(min=3, max=100)])
    age = IntegerField('age')
    nickname = StringField('nickname', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    fullname = StringField('fullname', validators=[InputRequired(), Length(min=4, max=150)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    nickname = StringField('nickname', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

# class 