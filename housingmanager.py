from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import base64
from base64 import b64encode
from flask_login import UserMixin, login_user, logout_user
from forms import RegistrationForm, LoginForm   #from forms.py import the RegistrationForm function
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_mail import Mail, Message

import os 


app = Flask(__name__)

mail = Mail(app)
bcrypt = Bcrypt(app)
dropzone = Dropzone(app)

#Mongo settings
app.config["MONGO_DBNAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

#email settings
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin jsepulvedadominguez@gmail.com'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

#Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'add_property' #I redirect to this route***

#Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  #set maximum file size, default is 16MB

mongo = PyMongo(app)

# @app.route("/")
# def home():
#     if "username" in session:
#         return "You are logged in as " + session["username"]
#     return render_template("login.html")
    

@app.route("/ad_type")
def filter_ad():

        type = request.args['type']
        if type=="rent":
            ads=mongo.db.ads.find({"rent": True})
            return render_template("filtered_properties.html", ads=ads)
            
        if type=="share":
            ads=mongo.db.ads.find({"share": True})
            return render_template("filtered_properties.html", ads=ads)
        
        if type=="buy":
            ads=mongo.db.ads.find({"sell": True})
            return render_template("filtered_properties.html", ads=ads)

@app.route("/my_ads")
def my_ads():
    ads = mongo.db.ads.find()
    return render_template("my_ads.html", ads=ads)


@app.route("/login", methods=["POST", "GET"])
def login():
    error=None
    form=LoginForm()
    if request.method == "POST": 
        users = mongo.db.users  #our collection
        user = users.find_one({"username": request.form["email"]})  #get the key-value pair in the document(dictionary) created.
        if user:
            if bcrypt.check_password_hash(user["password"], request.form["password"]):  #check password from login and from registration
                
                # login_user(user, form.remember_me.data)
                session["username"] = request.form["email"]  #I create my session 
                flash("You were successfully logged in!")
                return redirect(url_for('properties'))  
                
        error='Invalid username or password.'
        
    return render_template("login.html", form=form, error=error)


@app.route("/logout")
def logout():
    del session['username']
    return redirect(url_for('properties'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = mongo.db.users       #our collection
        existing_user = users.find_one({"username": request.form["email"]})
        
        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form["password"]).decode('utf-8')  #generate password  
            users.insert({"username": request.form["email"], "password": hashpass, "name": request.form["username"], "phone_number": request.form["phone_number"]}) #we instert the username and password into the user document
            session["username"] = request.form["email"]   #create my section so when we go to the line 18 (if "username" in session:) makes sense!!! 
            
            
            return redirect(url_for("add_property", existing_user=existing_user)) #MIGHT CHANGE THIS URL_FOR!!! as the "def home()" only returns that the username has logged in
        
        return "This username already exits."
    
    form=RegistrationForm() #form contains the RegistrationForm() function
    return render_template("register.html", form=form)
    
    
@app.route("/add_property", methods=["GET", "POST"])
def add_property():
    
    if request.method =="POST":
        facilities = request.form.getlist('property_facilities') #obtain facilities list
        file_obj = request.files 
        form_values = request.form.to_dict()
        
        image1 = request.files['image1']  
        image1_string = base64.b64encode(image1.read()).decode("utf-8")
        form_values["image1"] = "data:image/png;base64," + image1_string
        
        image2 = request.files['image2']  
        image2_string = base64.b64encode(image2.read()).decode("utf-8")
        form_values["image2"] = "data:image/png;base64," + image2_string
        
        image3 = request.files['image3']  
        image3_string = base64.b64encode(image3.read()).decode("utf-8")
        form_values["image3"] = "data:image/png;base64," + image3_string
        
        image4 = request.files['image4']  
        image4_string = base64.b64encode(image4.read()).decode("utf-8")
        form_values["image4"] = "data:image/png;base64," + image4_string
        
        image5 = request.files['image5']  
        image5_string = base64.b64encode(image5.read()).decode("utf-8")
        form_values["image5"] = "data:image/png;base64," + image5_string
        
        form_values["sell"] = "sell" in form_values   #true or false  
        form_values["rent"] = "rent" in form_values
        form_values["share"] = "share" in form_values
        
        user = mongo.db.users.find_one({"username": session["username"]}) #I have "username" stored in session so I use it to find that specific "username" from my users collection database. By finding the "username" I get its whole information and I assign it to the user variable that I just created.
        form_values["owner"] = {
            "email": user["username"],
            "phone_number": user["phone_number"],
            "name": user["name"]
        }
        
        
        form_values["property_facilities"]=facilities #insert facilities list in the doccument 

        ads = mongo.db.ads  #create my ads collection
        ads.insert(form_values) #insert data from the add_property form into the ads collection
        return redirect(url_for("properties"))
    else:
        return render_template("add_property.html")    

        
@app.route("/")
def properties():
    ads = mongo.db.ads.find()
    return render_template("properties.html", ads=ads)
    

@app.route("/ad_description/<ad_id>")
def ad_description(ad_id):
    ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) #I get the ad by its id
    return render_template("ad_description.html", ad=ad)    
    
    
@app.route("/properties/<ad_id>/edit", methods=["GET", "POST"])  #<ad_id> is passed from the properties.html  
def edit_ad(ad_id):
    if request.method == "POST":
        facilities = request.form.getlist('property_facilities') #obtain facilities list
        form_values = request.form.to_dict() #create a dictionary with the values of the form

        if "image1" in request.files:     #if there's an image inputted
            image1 = request.files['image1'] #I request that image
            image1_string = base64.b64encode(image1.read()).decode("utf-8")   # I transform the image into a string
            form_values["image1"] = "data:image/png;base64," + image1_string  #I add the image string to the value of the key "image" of the form_values dictionary 
        
        else:   #if there's no image input
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) #I get the ad by its id
            form_values["image1"] = old_ad["image1"]  #I assign the image that is in that ad to the dictionary form_values that has been updated
          
            
        if "image2" in request.files:     
            image2 = request.files['image2'] 
            image2_string = base64.b64encode(image2.read()).decode("utf-8")   
            form_values["image2"] = "data:image/png;base64," + image2_string  
        
        else:   
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) 
            form_values["image2"] = old_ad["image2"]  
            
        
        if "image3" in request.files:     
            image3 = request.files['image3'] 
            image3_string = base64.b64encode(image3.read()).decode("utf-8")   
            form_values["image3"] = "data:image/png;base64," + image3_string   
        
        else:   
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) 
            form_values["image3"] = old_ad["image3"]  
        
        
        if "image4" in request.files:     
            image4 = request.files['image4'] 
            image4_string = base64.b64encode(image4.read()).decode("utf-8")   
            form_values["image4"] = "data:image/png;base64," + image4_string   
        
        else:   
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) 
            form_values["image4"] = old_ad["image4"]  
            
            
        if "image5" in request.files:     
            image5 = request.files['image5'] 
            image5_string = base64.b64encode(image5.read()).decode("utf-8")   
            form_values["image5"] = "data:image/png;base64," + image5_string   
        
        else:   
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) 
            form_values["image5"] = old_ad["image5"]  
        
        
        form_values["sell"] = "sell" in form_values   #true or false  
        form_values["rent"] = "rent" in form_values
        form_values["share"] = "share" in form_values
        
        user = mongo.db.users.find_one({"username": session["username"]}) #I have "username" stored in session so I use it to find that specific "username" from my users collection database. By finding the "username" I get its whole information and I assign it to the user variable that I just created.
        form_values["owner"] = {
            "email": user["username"],
            "phone_number": user["phone_number"],
            "name": user["name"]
        }
        
        form_values["property_facilities"]=facilities #insert facilities list into the doccument 
        
        mongo.db.ads.update({"_id":ObjectId(ad_id)}, form_values) #I target the ad_id and update it with the form_values
        return redirect(url_for("properties"))
    
    else:
        
        the_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
        return render_template("edit_ad.html", the_ad=the_ad)
        
        
@app.route("/properties/<ad_id>/delete", methods=["POST"])
def delete_ad(ad_id):
    the_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
    mongo.db.ads.remove(the_ad)
    return redirect(url_for("properties"))
    

@app.route("/search", methods=["POST"])
def search_ad():
    
    if request.method == "POST":
        form_values = request.form.to_dict()
        town_to_search = request.form['town_to_search']
        purpose_to_search = request.form['purpose_to_search']
        type_to_search = request.form['type_to_search']
        
        ads = mongo.db.ads.find({ "town_name": {"$regex": town_to_search, "$options": 'i'}, purpose_to_search: True, "property_type": type_to_search})
        ads_number = mongo.db.ads.find({ "town_name": {"$regex": town_to_search, "$options": 'i'}, purpose_to_search: True, "property_type": type_to_search}).count()
        return render_template("searched_properties.html", ads=ads, ads_number=ads_number, town_to_search=town_to_search, purpose_to_search=purpose_to_search, type_to_search=type_to_search)
        
    
@app.route("/email")    
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template("properties.html", **kwargs)
    mail.send(msg)

# ad_owner_email

if __name__ == "__main__":
        
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)