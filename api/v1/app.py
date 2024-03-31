#!/usr/bin/python3
"""
This module is to get flask to start
"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask
app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000

@app.teardown_appcontext
def teardown_db(exception):
    """
    here after each request, this method calls
    .close() (i.e. .remove()) on the current
    SQLAlchemy Session
    """
    storage.close()


if __name__ == "___main__ ":
    """"Main Function"""
    app.run(host=host, port=port, threaded=True)
