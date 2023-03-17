from flask import flask

def create_app():
  app = Flask(_name_)
  app.config["key"] = "google"
  
  return app
