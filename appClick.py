from flask import *

app = Flask(__name__)

itemData = {49:'Ibuprofen', 39:'Crocin', 80:'Dolo', 120:'Gelusil', 100:'Accutane', 150:'Aspirin', 400:'Azathioprine', 749:'Citalopram', 1299:'Diazepam', 520:'Albuterol', 310:'Allegra', 60:'Benydryl'}

#every page extends base.html
#main home page
@app.route("/")
def home():
	return render_template("home.html")

#for register 
@app.route("/register")
def register():
	return render_template("register.html")

#for login
@app.route("/login")
def login():
	return render_template("login.html")

#for ordering meds
@app.route("/orderMeds")
def meds():
	return render_template("meds.html", itemData=itemData)

#for symptom tracker
@app.route("/symptomTrack")
def symptom():
	return render_template("symptom.html")

#for cart
@app.route("/cart")
def cart():
	return render_template("addtocart.html")

@app.route("/insurance")
def insurance():
	return render_template("insurance.html")

@app.route("/about")
def about():
	return render_template("about.html")

#timepass but do  not delete..it is for reference
# @app.route("/inner")
# def inner():
# 	return render_template("inner_page.html")


if __name__ == "__main__":
	app.run(debug=True)