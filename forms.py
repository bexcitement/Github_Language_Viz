
from wtforms import Form, TextField, TextAreaField, SubmitField, validators

class UserSubmit(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])

