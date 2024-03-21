from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,StringField,TextAreaField,FloatField,BooleanField,FloatField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed 
from flask_wtf.file import FileField, FileRequired



class UplaodMainCategoriesForm(FlaskForm):
    name = StringField('Enter the Name',validators=[DataRequired()])
    submit = SubmitField('Uplaod Main Categories Form')

class UplaodSubCategoriesForm(FlaskForm):
    name = StringField('Enter the Name',validators=[DataRequired()])
    submit = SubmitField('Uplaod Sub Categories Form')

class UplaodproductForm(FlaskForm):
    name = StringField('Enter the Name',validators=[DataRequired()])
    submit = SubmitField('Uplaod Product Form')

class UploadCompareForm(FlaskForm):
    name = StringField('Enter the Name',validators=[DataRequired()])
    submit = SubmitField('Uplaod Compare Form')

class DynamicFormProduct:
    @staticmethod
    def create_form(field_names,data):
        if data != None:
            class DynamicForm(FlaskForm):
                name = StringField('Name of product :', validators=[DataRequired()],default=data['name'])                
                price = FloatField('Price of product :', validators=[DataRequired()],default=data['price'])
                
                brand= StringField('Brand :' ,validators=[DataRequired()],default=data['brand']) 
                productid= StringField('Enter the ID :' ,validators=[DataRequired()],default=data['productid']) 
                description = TextAreaField('Description of product :', validators=[DataRequired()],default=data['discription'],render_kw={"rows": 15, "cols": 50})
                height = FloatField('Height of product :',validators=[DataRequired()],default=data['height'])
                width = FloatField('Width of product :',validators=[DataRequired()],default=data['width'])
                weight = FloatField('Weight of product :',validators=[DataRequired()],default=data['weight'])
                minimumOrderUnit= FloatField('Minimum order quantity :', validators=[DataRequired()],default=data['minimumOrderUnit'])
                top = BooleanField('Top',default=data['top'])
            for field_name in field_names:
                field_label = field_name['name']
                try:
                    field_default = data['compare_parameter'][field_name['name']]
                except:
                    field_default = None
                setattr(DynamicForm, field_name['name'], StringField(field_label, default=field_default))
            return DynamicForm()
        else:
            class DynamicForm(FlaskForm):
                name = StringField('Name of product :')
                brand= StringField('Brand :' ,validators=[DataRequired()]) 
                price = FloatField('Price of product :', validators=[DataRequired()])
                productid= StringField('Enter the ID :' ,validators=[DataRequired()]) 
                minimumOrderUnit= FloatField('Minimum order quantity :', validators=[DataRequired()],render_kw={"rows": 15, "cols": 50})
                description = TextAreaField('Description of product :')
                height = FloatField('Height of product :',validators=[DataRequired()])
                width = FloatField('Width of product :',validators=[DataRequired()])
                weight = FloatField('Weight of product :',validators=[DataRequired()])
                top = BooleanField('Top')
                photos1 = FileField('Photos (635px X 563px)', validators=[DataRequired(),FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
                photos2 = FileField('Photos (635px X 563px)', validators=[DataRequired(),FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
                photos3 = FileField('Photos (635px X 563px)', validators=[DataRequired(),FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
                photos4 = FileField('Photos (635px X 563px)', validators=[DataRequired(),FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
            for field_name in field_names:
                setattr(DynamicForm, field_name['name'], StringField( field_name['name']))
            return DynamicForm()

class UploadForm(FlaskForm):
    name = StringField('Name')
    file = FileField('Image', validators=[FileRequired()])
    submit=SubmitField('Upload')