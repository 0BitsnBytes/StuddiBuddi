from flask import Flask, render_template, redirect, session, request
from flask_session import Session
from bardapi import Bard
import requests , json

x = None

Username = ["Samarth","Mudith"]
Password = ["is","Einstien2.0"]

app = Flask(__name__)
app.secret_key = "BroLikesSchoolFood#6942"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
  return redirect("/Login")

@app.route("/Login")
def Login():
  return render_template("login.html")

@app.route("/process" , methods=["POST"])
def process():
  Value = request.form
  if Value["Username"] in Username and Value["Password"] in Password:
    session["user"] = Value["Username"]
    return render_template("homepage.html")
  else:
    return render_template("loginDen.html")
  
@app.route("/query", methods=["POST"])
def Query():
  url = "https://profanity-cleaner-bad-word-filter.p.rapidapi.com/profanity"
  x = request.form["Query"].strip()
  payload = {
    "text": x,
    "maskCharacter": "*",
    "language": "en"
  }
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "8631403470mshd95960d1294af1ap1b37cbjsn5c0a2d143b60",
    "X-RapidAPI-Host": "profanity-cleaner-bad-word-filter.p.rapidapi.com"
  }

  response = requests.post(url, json=payload, headers=headers).json()
  if not response["profanities"]:
    Var=(Bard(token = "fwilwx1fjOC0z04elgwEaJiQzLdSjuj2k04L3SH06M2_XZBmfLd43gdLGDIj6R21eCW0ig.")).get_answer(f'Give a hint for the answer to the question in one line {x}. Do not give the answer.')
    return render_template("answers.html",Var=Var["content"],aer=x)
  else:
    return render_template("homepageIsBad.html")
  
@app.route("/proc",methods=["POST"])
def proc():
  x = request.form["Val"]
  return render_template("answer.html",Var = (Bard(token = "fwilwx1fjOC0z04elgwEaJiQzLdSjuj2k04L3SH06M2_XZBmfLd43gdLGDIj6R21eCW0ig.")).get_answer(f'Give a answer to the question "{x}" in 1 line only as text')["content"])


app.run(debug=True)
