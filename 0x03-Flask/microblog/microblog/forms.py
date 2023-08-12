from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo
from wtforms.validators import ValidationError

from microblog.models import User


class LoginForm(FlaskForm):
    """A LoginForm class definition."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """A RegistrationForm class definition."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_2 = PasswordField('Repeat Password', validators=[DataRequired(),
                                                             EqualTo('password')]
                              )
    submit = SubmitField('Register')

    def validate_username(self, username):
        """checks validation of username."""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("username taken, please choose "
                                  "a different username")

    def validate_email(self, email):
        """checks validation of email."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("email address already exists, "
                                  "please use a different email address.")
