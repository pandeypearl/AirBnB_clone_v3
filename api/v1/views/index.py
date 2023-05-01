#!/usr/bin/python3
""" Initializes flask functions """
from flask import jsonify, make_response
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def view_status():
	""" Returns JSON """
	response = jsonify({"status": "OK"})
	response.headers["Content-Type"] = "application/json"
	return response
