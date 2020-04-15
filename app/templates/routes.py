from flask import render_templates
from app import app
import datetime
@app.route("/",methods=["GET"])
def index():
    details ={'user':'kb'}
    return render_template("index.html")