from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, validators, TextAreaField
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from wtforms.fields import SelectField
from app.models import User, Post

def my_length_check(form, field):
    if len(field.data) > 12:
        raise ValidationError('Field must be less than 12 characters')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name        = StringField('Name', validators=[DataRequired()])
    birthday    = DateField('Birthday', format='%Y-%m-%d',validators=[DataRequired()])
    gender      = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    phone       = StringField('Mobile Phone', validators=[DataRequired(), my_length_check])
    username = StringField('Username', validators=[DataRequired()])
    email       = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name        = StringField('Name', validators=[DataRequired()])
    birthday    = DateField('Birthday', format='%Y-%m-%d',validators=[DataRequired()])
    gender      = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    phone       = StringField('Mobile Phone', validators=[DataRequired(), my_length_check])
    username = StringField('Username', validators=[DataRequired()])
    email       = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    post = TextAreaField('Post Something:', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Post')
