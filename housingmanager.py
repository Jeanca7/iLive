from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import base64
from base64 import b64encode
from flask_login import UserMixin, login_user, logout_user
from forms import RegistrationForm, LoginForm   #from forms.py import the RegistrationForm function 

app = Flask(__name__)
bcrypt = Bcrypt(app)


app.config["MONGO_DBNAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

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
            return render_template("properties.html", ads=ads)
            
        if type=="share":
            ads=mongo.db.ads.find({"share": True})
            return render_template("properties.html", ads=ads)
        
        if type=="buy":
            ads=mongo.db.ads.find({"sell": True})
            return render_template("properties.html", ads=ads)

@app.route("/my_ads")
def my_ads():
    ads = mongo.db.ads.find()
    return render_template("my_ads.html", ads=ads)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": 
        users = mongo.db.users  #our collection
        login_user = users.find_one({"username": request.form["email"]})  #get the key-value pair in the document(dictionary) created.
        if login_user:
            if bcrypt.check_password_hash(login_user["password"], request.form["password"]):  #check password from login and from registration
                print("success")
                session["username"] = request.form["email"]  #I create my session 
                return redirect(url_for("properties"))                    #will change this for properties  
                    
        return "invalid username/password combination"
    form=LoginForm()
    return render_template("login.html", form=form)


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
        image = request.files['image']  
        image_string = base64.b64encode(image.read()).decode("utf-8")
        
        form_values = request.form.to_dict()
        
        form_values["image"] = "data:image/png;base64," + image_string  
        
        form_values["sell"] = "sell" in form_values   #true or false  
        form_values["rent"] = "rent" in form_values
        form_values["share"] = "share" in form_values
        
        user = mongo.db.users.find_one({"username": session["username"]}) #I have "username" stored in session so I use it to find that specific "username" from my users collection database. By finding the "username" I get its whole information and I assign it to the user variable that I just created.
        form_values["owner"] = {
            "email": user["username"],
            "phone_number": user["phone_number"],
            "name": user["name"]
        }
         
        
        ads = mongo.db.ads  #create my ads collection
        ads.insert(form_values) #insert data from the add_property form into the ads collection
        return redirect(url_for("properties"))
    else:
        return render_template("add_property.html")    
        
@app.route("/")
def properties():
    ads = mongo.db.ads.find()
    return render_template("properties.html", ads=ads)
    
    
@app.route("/properties/<ad_id>/edit", methods=["GET", "POST"])  #<ad_id> is passed from the properties.html  
def edit_ad(ad_id):
    if request.method == "POST":
        
        form_values = request.form.to_dict() #create a dictionary with the values of the form
        
        if "image" in request.files:     #if there's an image inputted
            image = request.files['image'] #I request that image
            image_string = base64.b64encode(image.read()).decode("utf-8")   # I transform the image into a string
            form_values["image"] = "data:image/png;base64," + image_string  #I add the image string to the value of the key "image" of the form_values dictionary 
        
        else:   #if there's no image inputted
            old_ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)}) #I get the ad
            form_values["image"] = old_ad["image"]  #I assign the image that is in that ad to the dictionary form_values that has been updated 
        
        form_values["sell"] = "sell" in form_values   #true or false  
        form_values["rent"] = "rent" in form_values
        form_values["share"] = "share" in form_values
        # form_values["owner"]=session["username"]  #I insert the owner key-value
        user = mongo.db.users.find_one({"username": session["username"]}) #I have "username" stored in session so I use it to find that specific "username" from my users collection database. By finding the "username" I get its whole information and I assign it to the user variable that I just created.
        form_values["owner"] = {
            "email": user["username"],
            "phone_number": user["phone_number"],
            "name": user["name"]
        }
        
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


if __name__ == "__main__":
        app.secret_key = "jeanko"
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)