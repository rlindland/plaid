from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    access_token = StringField('Access Token', validators=[DataRequired()])
    item_id = StringField('Item ID', validators=[DataRequired()])
    submit = SubmitField('Sign In')