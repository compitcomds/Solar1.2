from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,StringField,TextAreaField,URLField
from wtforms.validators import DataRequired,Regexp
from flask_wtf.file import FileField, FileAllowed




class UploadArrivals(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    video_url = URLField('Video URL', validators=[DataRequired('URL is required')])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Upload Arrivals')


