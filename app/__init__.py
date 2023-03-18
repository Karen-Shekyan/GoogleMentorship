from flask import Flask, render_template, session, request, redirect,
import requests, os, json

app = Flask(__name__)

@app.route('/')
def log_in():
    if 'username' in session:
        return redirect('/home')
    return render_template('login.html') #For login AND signup

@app.route('/home')
def home():
    if (session):
        return render_template('home.html', user = 'username')
    else:
        return redirect('/')

# def create_app():
#   app = Flask(__name__)
#   app.config["key"] = "google" what is this???
#
#   from .views import views
#   from .auth import auth
#
#   # used to create prefixes for the different webpages
#   # app.register_blueprint(views, url_prefix='/')
#   # app.register_blueprint(auth, url_prefix='/')
#
#   return app

if __name__ == "__main__": #used to execute the file
  app.run(debug=True)
