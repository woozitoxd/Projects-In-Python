from flask import Flask
from .main.routes import main
from .users.routes import users

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(users)
    return app
