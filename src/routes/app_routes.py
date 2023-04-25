"""This module contains all the functional api routes related to application."""
import logging

from flask import Blueprint, jsonify, request

app_apis = Blueprint("app_apis", __name__)

ROUTES = {
    "test": "/test",
    "home": "/",
}
METHODS = {
    "get": ["GET"],
    "post": ["POST"],
}

@app_apis.route(ROUTES["test"], methods=METHODS["get"])
@app_apis.route(ROUTES["home"], methods=METHODS["get"])
def test():
    """
    This is a test API to check if application is running or not. A 200 status code will suffice
    that application is working.
    return: tuple
    """
    message = "Application is up and running."
    identifier = request.form.get("identifier", default="generic", type=str)
    logger = logging.getLogger(identifier)
    logger.info(message)
    return jsonify(contents="Success", message=message, data={}), 200
