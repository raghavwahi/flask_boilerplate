"""This is a flask application boilerplate."""
from flask import Flask, request

from src.routes.app_routes import app_apis
from src.utils.logger_util import Logger

app = Flask(__name__)
app.register_blueprint(app_apis)


@app.before_request
def init_logging_obj():
    """This middleware initializes logger object based on identifier."""
    identifier = request.form.get("identifier", default="generic", type=str)
    Logger(identifier)  # Update file handler to write logs in identifier based file.


if __name__ == "__main__":
    app.run(threaded=True)
