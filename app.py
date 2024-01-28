from flask import Flask, render_template, redirect, session, request
from flask_session import Session

app = Flask(__name__)
Passwords = ""

@app.route("/")
def Login():
  return "hello"

app.run(debug=True)
