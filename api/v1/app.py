#!/usr/bin/python3
"""
This module is to stat=rt the app
"""
from flask import Flask
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    calls storage.close()
    """
    storage.close()


if __name__ == "__main__":
    """
    Main App
    """
    app.run(host=host, port=port)
