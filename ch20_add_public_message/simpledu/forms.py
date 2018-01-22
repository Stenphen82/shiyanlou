from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField,IntegerField
from wtforms.validators import Length, Email, EqualTo, Required,URL,NumberRange
from simpledu.models import db, User,Course,Live
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

    def update_user(self,user):
        self.populate_obj(user)
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

class CourseForm(FlaskForm):
    name=StringField('CourseName',validators=[Required(),Length(5,32)])
    description = TextAreaField('CourseDescription',validators=[Required(),Length(20,256)])
    image_url = StringField('CoverImage',validators=[Required(),URL()])
    author_id=IntegerField('AuthorID',validators=[Required(),NumberRange(min=1,message='InvalidUserID')])
    submit = SubmitField('Submit')

    def validate_author_id(self,field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('UserNotFound')

    def create_course(self):
        course=Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self,course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

class UserForm(FlaskForm):
    username = StringField('UserName',validators=[Required(),Length(3,24)])
    email=StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('RepeatPassword',validators=[Required(),EqualTo('password')])
    role=IntegerField('RolePrivilege',validators=[Required(),NumberRange(min=10,message=    'InvalidRoleID')])
    job=StringField('Job',validators=[Required(),Length(3,24)])
    submit=SubmitField('Submit')
    
    def create_user(self):
        user=User() 
        user.username=self.username.data
        user.email=self.email.data
        user.password=self.password.data
        user.role = self.role.data
        user.job=self.job.data
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_user(self,user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
         
class LiveForm(FlaskForm):
    name=StringField('LiveName',validators=[Required(),Length(1,256)])
    user_id = IntegerField('AuthorID',validators=[Required(),NumberRange(min=1,message='InvalidUserID')])
    submit = SubmitField('Submit')

    def validate_author_id(self,field):
        if not User.query.get(self.anchor.data):
            raise ValidationError('UserNotFound')

    def create_live(self):
        live=Live()
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live


         

