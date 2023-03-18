from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home(): # function that creates the home page
    return "<h1>Test</h1>"
