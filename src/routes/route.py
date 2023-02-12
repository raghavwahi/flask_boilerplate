from flask import Blueprint

initial_route = Blueprint('initial_route', __name__)

@initial_route.route('/ping')
def ping():
    return "Application is running"