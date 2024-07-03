from flask import Blueprint, jsonify,abort,render_template,redirect,url_for, request,flash
from flask_login import login_required,current_user
from Solar.database import db
from Solar.Banner.form import UploadForm
from Solar.NewArrivals.form import UploadArrivals
from bson import ObjectId

NewArrival=Blueprint('NewArrivals',__name__,template_folder='templates/arrivals',static_folder='')

@NewArrival.before_request
@login_required
def check_is_User():
    id=current_user.user_id
    if not(current_user.is_authenticated  and current_user.role=='Admin'):
        return "<h1>this is invalid</h1>","403"
    
@NewArrival.route('/Arrivals',methods=['GET','POST'])
def addArrival():
    
    # req= request.args['isupdate']
    # if req:
    #     print(req)
    form=UploadArrivals()
    if form.validate_on_submit():
        data= {
            'title':form.title.data,
            'video_url': form.video_url.data,
            'description':form.description.data,
        }
        db.NewArrivals.insert_one(data)
        return render_template('showarrivals.html')
    return render_template('Arrivals.html',form=form)



    
@NewArrival.route('/')
def showarrivals():
    data = db.NewArrivals.find()
    print(data)
    return render_template('showarrivals.html',data=data)

@NewArrival.route('/deletearrival/<arrival_id>')
def deleteArrival(arrival_id):
    result = db.NewArrivals.delete_one({'_id': ObjectId(arrival_id)})
    if result.deleted_count > 0:
        flash('Deleted successfully', 'success')
    else:
        flash('Not able to delete', 'error')
    return redirect(url_for('NewArrivals.showarrivals'))
    
