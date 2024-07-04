from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,StringField,TextAreaField,FloatField,BooleanField,FloatField,IntegerField
from wtforms.validators import DataRequired ,NumberRange
from flask_wtf.file import FileField, FileAllowed 
from flask_wtf.file import FileField, FileRequired



class UplaodMainCategoriesForm(FlaskForm):
    name = StringField('Enter the Name',validators=[DataRequired(message='Name is required')])
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
                name = StringField('Name of product:', default=data['name'] or "")                
                price = FloatField('Price of product:', default=data['price']or 0)
                brand = StringField('Brand:',  default=data['brand'] or "") 
                productid = StringField('Enter the ID:',  default=data['productid'] or "") 
                description = TextAreaField('Description of product:',  default=data['discription'] or  "", render_kw={"rows": 15, "cols": 50})
                height = FloatField('Height of product:', default=data['height'] or 0)
                length = FloatField('Length of product:', default=data['length']or 0)
                breadth = FloatField('Breadth of product:', default=data['breadth']or 0)
                weight = FloatField('Weight of product:', default=data['weight']or 0)
                minimumOrderUnit = FloatField('Minimum order quantity:', default=data['minimumOrderUnit']or 0)
                top = BooleanField('Top', default=data['top'])
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
                name = StringField('Name of product:', validators=[DataRequired(message="Name is required.")],default= "")
                brand = StringField('Brand:', validators=[DataRequired(message="Brand is required.")],default= "")
                price = FloatField('Price of product:',default=0)
                productid = StringField('Enter the ID:', validators=[DataRequired(message="Product ID is required.")],default= "")
                minimumOrderUnit = FloatField('Minimum order quantity:', default= 0, render_kw={"rows": 15, "cols": 50})
                description = TextAreaField('Description of product:',default= "")
                height = FloatField('Height of product:',default= 0)
                length = FloatField('Length of product:',default= 0)
                breadth = FloatField('Breadth of product:',default= 0)
                weight = FloatField('Weight of product:',default= 0)
                top = BooleanField('Top')
                photos1 = FileField('Photos 1', validators=[ DataRequired(),FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos2 = FileField('Photos 2', validators=[ DataRequired(),FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos3 = FileField('Photos 3', validators=[ DataRequired(),FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos4 = FileField('Photos 4', validators=[ DataRequired(),FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
            for field_name in field_names:
                setattr(DynamicForm, field_name['name'], StringField( field_name['name']))
            return DynamicForm()

class UploadForm(FlaskForm):
    name = StringField('Name')
    file = FileField('Image', validators=[FileRequired()])
    submit=SubmitField('Upload')