from a1_app import application
from flask import render_template,request,redirect,url_for


@application.route('/', methods=['GET', 'POST'])
def home():
    contents = {
      'content':"Car Price Prediction "
    }
    return render_template('home.html', **contents)
