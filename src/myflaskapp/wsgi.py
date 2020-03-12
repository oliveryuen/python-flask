"""WSGI module"""
from myflaskapp import create_app

APPLICATION = create_app()

if __name__ == "__main__":
    APPLICATION.run(host="localhost", port=5000, debug=True, use_reloader=True)
