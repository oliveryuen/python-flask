from dynaconf import FlaskDynaconf
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump


def register_blueprints(app):
    from .views.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)
    HealthCheck(app, "/healthcheck")
    EnvironmentDump(app, "/environment")
    register_blueprints(app)
    return app

