from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField,RadioField,FileField,URLField
from wtforms.validators import DataRequired
from wtforms import  SubmitField

class UploadForm(FlaskForm):
    url=URLField('Enter URL', validators=[DataRequired()])
    file = FileField('Image', validators=[DataRequired()])
    submit=SubmitField('Upload')