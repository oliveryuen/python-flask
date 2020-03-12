"""Flask RestPlus API Wrapper"""
from flask_restplus import Api
from flask import url_for


class MyApi(Api):
    """
    Fix for swagger.json behind reverse proxy:
    https://github.com/noirbizarre/flask-restplus/issues/223#issuecomment-381439513
    """

    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)
