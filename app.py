from flask import Flask, render_template, redirect, session, request
from flask_session import Session

app = Flask(__name__)
app.secret_key = "BroLikesSchoolFood#6942"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
  return redirect("/Login")

@app.route("/Login")
@app.route("/login")
def Login():
  return render_template("login.html")

@app.route("/process" , methods=["POST"])
def process():
  Value = request.form
  return Value

app.run(debug=True)
