from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import Vis


class RegisterForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min = 6 , max = 30),DataRequired()])
    email_address = StringField(label='Email Address:',validators = [Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min = 6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')
    
    def validate_username(self,user):
        user1 = Vis.query.filter_by(username =user.data).first()
        if user1:
            raise ValidationError('Username already exist!')
    
    def validate_email(self, email):
        email1 = Vis.query.filter_by(email_address=email.data).first()
        if email1:
            raise ValidationError('Email already exists!')

class LoginForm(FlaskForm):
    username = StringField(label = 'User Name', validators=[DataRequired()])
    password = PasswordField(label = 'Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
     submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
     submit = SubmitField(label='Sell Item')