from flask import render_template
from app import app
@app.route("/",methods=["GET"])
def index():
    details ={'user':'kb'}
    return render_template('index.html')