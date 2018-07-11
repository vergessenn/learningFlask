import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("next.html")

@app.route("/back")
def back():
    return render_template("index.html")
