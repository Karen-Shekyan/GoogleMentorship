from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login') # login route
def login(): # function to make the login
    return "<p>Login</p>"

@auth.route('/logout') # logout route
def logout(): 
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"