"""This module contains all the functional api routes related to application."""
from flask import Blueprint, jsonify

application_apis = Blueprint("application_apis", __name__)

ROUTES = {
    "test": "/test",
    "home": "/",
}
METHODS = {
    "get": ["GET"],
    "post": ["POST"],
}

@application_apis.route(ROUTES["test"], methods=METHODS["get"])
@application_apis.route(ROUTES["home"], methods=METHODS["get"])
def test():
    """
    This is a test API to check if application is running or not. A 200 status code will suffice
    that application is working.
    return: tuple
    """
    message = "Application is up and running."
    return jsonify(contents="Success", message=message, data={}), 200
