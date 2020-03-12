"""myflaskapp module"""
from dynaconf import FlaskDynaconf
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump


def register_blueprints(app) -> None:
    """
    Register blue prints for the Flask app
    :param app: Flask app
    :return: None
    """
    from .views.forex_api import FOREX_API_BLUEPRINT
    app.register_blueprint(FOREX_API_BLUEPRINT, url_prefix='/api/forex')


def create_app():
    """
    Creates the Flask app
    :return: Flask app
    """
    app = Flask(__name__)
    FlaskDynaconf(app)
    HealthCheck(app, "/healthcheck")
    EnvironmentDump(app, "/environment")
    register_blueprints(app)
    return app
