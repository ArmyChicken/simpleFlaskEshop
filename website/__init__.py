from flask import Flask
from os import path

def create_app():
    app = Flask (__name__)
    app.config["SECRET_KEY"] ="sikrit ki"

    

    return app