from dynaconf import FlaskDynaconf
from flask import Flask


def register_blueprints(app):
    from .views.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)
    register_blueprints(app)
    return app

