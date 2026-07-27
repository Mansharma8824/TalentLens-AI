from flask import Flask
from app.routes import resiter_routes

def create_app():
    app = Flask(__name__)
    resiter_routes(app)
    
    return app