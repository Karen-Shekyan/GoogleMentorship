from flask import Flask, render_template, session, request, redirect, url_for
import requests, os, json
from database import *

app = Flask(__name__)
app.secret_key = os.urandom(32) # This is NOT secure. MUST FIX

@app.route('/')
def log_in():
    if 'username' in session: # If already logged in
        return redirect('/home')
    return render_template('login.html') # For login AND signup

@app.route('/home')
def home():
    if (session): # If logged in, show the home page
        return render_template('home.html', user = session['username'])
    else: # ...else show the login page
        return redirect('/')

@app.route('/login', methods = ["POST"])
def authenticate():
    if 'username' in session:
        return render_template('home.html', user = 'username')
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
    if request.method == 'GET':
        user = request.args['username']
        pw = request.args['password']
    if login(user,pw):
        if request.method == 'POST':
            session['username'] = request.form['username']
        if request.method == 'GET':
            session['username'] = request.args['username']
        return redirect('/home')
    else:
        return render_template('login.html', errorTextL= "Please enter a valid username and password")

@app.route('/signup', methods = ["POST"])
def sign_up():
    if 'username' in session:
        return render_template('home.html', user = 'username')
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        email = request.form['email']
    if request.method == 'GET':
        user = request.args['username']
        pw = request.args['password']
        email = request.args['email']
    if '@' in email and '.' in email.split('@')[1]:
        if signup(user,pw,email):
            return render_template('login.html')
        else:
            return render_template('login.html', errorTextS= "User already exists")
    else:
        return render_template('login.html', errorTextS = "Invalid email")

# def create_app():
#   app = Flask(__name__)
#   app.config["key"] = "google" #what is this???
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
