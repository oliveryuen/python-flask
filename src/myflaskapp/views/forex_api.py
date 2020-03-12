"""REST API for Forex"""
from flask import Blueprint, jsonify
from flask_restplus import Resource

from .my_api import MyApi
from ..core.forex import get_usd_rate


FOREX_API_BLUEPRINT = Blueprint('forex_api', __name__)
API = MyApi(FOREX_API_BLUEPRINT,
            description="REST API for Forex functionalities",
            doc="/doc",
            title="Forex API"
            )


@API.route("/rates/usd")
class USDRate(Resource):

    @classmethod
    def get(cls):
        """
        Get latest exchange rates with respect to USD
        :return: List of exchange rates
        """
        return jsonify("usd", get_usd_rate())
