"""This module contains all the functional api routes related to application."""
import logging

from flask import Blueprint, jsonify, request

from src.utils.helpers import fetch_request_methods

app_apis = Blueprint("app_apis", __name__)

ROUTES = {
    "test": "/test",
    "home": "/",
}
METHODS = fetch_request_methods()

@app_apis.route(ROUTES["test"], methods=METHODS["post"])
@app_apis.route(ROUTES["home"], methods=METHODS["post"])
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
