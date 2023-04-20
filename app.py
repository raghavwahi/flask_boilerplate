"""This is a flask application boilerplate."""
from flask import Flask

from src.routes.routes_app import application_apis

app = Flask(__name__)
app.register_blueprint(application_apis)


if __name__ == "__main__":
    app.run(threaded=True)
