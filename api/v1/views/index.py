#!/usr/bin/python3
"""This module is for index"""
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns status
    """
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)