"""This is a flask application boilerplate."""
from flask import Flask

from src.routes.route import initial_route

app = Flask(__name__)
app.register_blueprint(initial_route)

# TODO: Add logging logic
# TODO: Add a check if all dependent modules are installed or not in src/__init__.py
# TODO: Add config parser
# TODO: Add a config file
# TODO: Add a before request handler


if __name__ == "__main__":
    app.run(debug=True)