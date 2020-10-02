from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

itemData = {1:'Iboprofin', 2:'Crocin', 3:'Dolo', 4:'Gelusil', 5:'a', 6:'b', 7:'c', 8:'d', 9:'e', 10:'f', 11:'g', 12:'h'}

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


#timepass but do  not delete..it is for reference
# @app.route("/inner")
# def inner():
# 	return render_template("inner_page.html")


if __name__ == "__main__":
	app.run(debug=True)