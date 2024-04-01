#!/usr/bin/python3
"""
This module is to stat=rt the app
"""
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from werkzeug.exceptions import HTTPException
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)
swagger = Swagger(app)

app.url_map.strict_slashes = False

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

cors = CORS(app, resources={r'/*': {'origins': host}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    calls storage.close()
    """
    storage.close()


@app.errorhandler(Exception)
def global_error_handler(err):
    """
    Global  Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
    return make_response(jsonify(message), code)


def setup_global_errors():
    """
    This updates HTTP Exception Class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == "__main__":
    """
    Main App
    """
    setup_global_errors()
    app.run(host=host, port=port)
