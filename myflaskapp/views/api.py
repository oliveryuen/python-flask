from flask import Blueprint
from flask_restplus import Api, Resource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, doc="/doc")


@api.route("/hello")
class Hello(Resource):
    """Gets the hello message"""

    def get(self):
        return {
            "message": "Hello!"
        }

