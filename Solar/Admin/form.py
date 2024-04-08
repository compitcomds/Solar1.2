from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,StringField,TextAreaField,FloatField,BooleanField,FloatField,IntegerField
from wtforms.validators import DataRequired
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
                name = StringField('Name of product:', validators=[DataRequired(message="Please enter the name of the product.")], default=data['name'])                
                price = FloatField('Price of product:', validators=[DataRequired(message="Please enter the price of the product."), NumberRange(min=0, message="Price must be a positive number.")], default=data['price'])
                brand = StringField('Brand:', validators=[DataRequired(message="Please enter the brand of the product.")], default=data['brand']) 
                productid = StringField('Enter the ID:', validators=[DataRequired(message="Please enter the ID of the product.")], default=data['productid']) 
                description = TextAreaField('Description of product:', validators=[DataRequired(message="Please enter the description of the product.")], default=data['discription'], render_kw={"rows": 15, "cols": 50})
                height = FloatField('Height of product:', validators=[DataRequired(message="Please enter the height of the product.Height must be a positive number."), NumberRange(min=0, message="Height must be a positive number.")], default=data['height'])
                length = FloatField('Length of product:', validators=[DataRequired(message="Please enter the length of the product.Length must be a positive number."), NumberRange(min=0, message="Length must be a positive number.")], default=data['length'])
                breadth = FloatField('Breadth of product:', validators=[DataRequired(message="Please enter the breadth of the product.Breadth must be a positive number."), NumberRange(min=0, message="Breadth must be a positive number.")], default=data['breadth'])
                weight = FloatField('Weight of product:', validators=[DataRequired(message="Please enter the weight of the product. Weight must be a positive number."), NumberRange(min=0, message="Weight must be a positive number.")], default=data['weight'])
                minimumOrderUnit = FloatField('Minimum order quantity:', validators=[DataRequired(message="Please enter the minimum order quantity."), NumberRange(min=0, message="Minimum order quantity must be a positive number.")], default=data['minimumOrderUnit'])
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
                name = StringField('Name of product:', validators=[DataRequired(message="Name is required.")])
                brand = StringField('Brand:', validators=[DataRequired(message="Brand is required.")])
                price = FloatField('Price of product:', validators=[DataRequired(message="Price is required.")])
                productid = StringField('Enter the ID:', validators=[DataRequired(message="Product ID is required.")])
                minimumOrderUnit = FloatField('Minimum order quantity:', validators=[DataRequired(message="Minimum order quantity is required.")], render_kw={"rows": 15, "cols": 50})
                description = TextAreaField('Description of product:')
                height = FloatField('Height of product:', validators=[DataRequired(message="Height is required. Height must be a positive number.")])
                length = FloatField('Length of product:', validators=[DataRequired(message="Length is required. Length must be a positive number.")])
                breadth = FloatField('Breadth of product:', validators=[DataRequired(message="Breadth is required. Breadth must be a positive number.")])
                weight = FloatField('Weight of product:', validators=[DataRequired(message="Weight is required. Weight must be a positive number.")])
                top = BooleanField('Top')
                photos1 = FileField('Photos 1', validators=[DataRequired(message="Photo 1 is required."), FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos2 = FileField('Photos 2', validators=[DataRequired(message="Photo 2 is required."), FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos3 = FileField('Photos 3', validators=[DataRequired(message="Photo 3 is required."), FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
                photos4 = FileField('Photos 4', validators=[DataRequired(message="Photo 4 is required."), FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, or PNG files allowed.")])
            for field_name in field_names:
                setattr(DynamicForm, field_name['name'], StringField( field_name['name']))
            return DynamicForm()

class UploadForm(FlaskForm):
    name = StringField('Name')
    file = FileField('Image', validators=[FileRequired()])
    submit=SubmitField('Upload')