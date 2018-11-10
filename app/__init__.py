from flask import Blueprint,Flask
from .api.v1 import version1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(version1)
    return app