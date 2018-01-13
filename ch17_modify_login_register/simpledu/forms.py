from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User
import re


class RegisterForm(FlaskForm):
    username = StringField('UserName',validators=[Required(),Length(3,24)])
    email=StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('RepeatPassword',validators=[Required(),EqualTo('password')])
    submit=SubmitField('Submit')

    def create_user(self):
        user=User()
        user.username=self.username.data
        user.email=self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user


    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('User already exists')
        elif not bool(re.match('^[0-9a-zA-Z]+$',field.data)):
            raise ValidationError('username can only contain digits or alphabets')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
   #email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    password = PasswordField('Password',validators=[Required(),Length(6,24)]    )
    remember_me = BooleanField('RememberMe')
    submit = SubmitField('Submit')

   # def validate_email(self,field):
       # if field.data and not User.query.filter_by(email=field.data).first():
           # raise ValidationError('Email has not registered')

    def validate_username(self,field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('user not found')

    def valdiate_password(self,field):
        user=User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password Error')
