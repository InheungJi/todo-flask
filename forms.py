from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo


class TodoForm(FlaskForm):
    todo = StringField("Todo: ", validators=[DataRequired()])
    submit = SubmitField("Add Todo")


class RegistrationForm(FlaskForm):
    username = StringField("User name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    password2 = PasswordField("Repeat Password: ", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("ID: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")

