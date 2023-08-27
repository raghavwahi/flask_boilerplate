"""This module contains test configuration."""
import pytest

from app import app as flask_app


@pytest.fixture
def app():
    """This function yields flask app after setting up its context."""
    flask_app.app_context()
    yield flask_app


@pytest.fixture()
def client(app):  # pylint: disable=redefined-outer-name
    """
    This function returns a test client to execute test cases on the app.
    args:
        app: function
    return: app test client
    """
    # Add steps to set up test environment.
    return app.test_client()
