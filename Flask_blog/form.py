from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
import email_validator
from Flask_blog.models import User

class RegistrationForm(FlaskForm):
	full_name = StringField('Full Name',validators=[Length(min=2,max=30),DataRequired()])
	user_name = StringField('User Name',validators=[Length(min=2,max=30),DataRequired()])
	email = StringField('Email',validators=[Email(),DataRequired()])
	password =StringField('Password',validators=[DataRequired()])
	confirm_password =StringField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_user_name(self, user_name):
		user_1 = User.query.filter_by(user_name=user_name.data).first()
		if user_1:
			raise ValidationError(f'This User Name has been token please use an other one.')
	
	def validate_email(self, email):
		user_1 = User.query.filter_by(email=email.data).first()
		if user_1:
			raise ValidationError(f'This Email has been token please use an other one.')


class LoginForm(FlaskForm):
	# user_name = StringField('User Name',validators=[Length(min=2,max=30),DataRequired()])
	email = StringField('Email',validators=[Email(),DataRequired()])
	password =StringField('Password',validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Login')


	