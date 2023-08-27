"""This module test '/' and '/test' routes of the application."""
import json

def __prepare_payload():
    """
    This function prepares payload for the requests.
    args: None
    return: dict
    """
    return {"identifier": "test_identifier"}


def test_home_identifier(client):
    """
    This function tests '/' route of the application with an identifier provided.
    args:
        client: pytest fixture
    return: None
    """
    route = "/"
    response = client.post(route, data=__prepare_payload())
    contents = json.loads(response.data)["contents"]
    assert "Success" in contents
    assert  response.status_code == 200


def test_home_without_identifier(client):
    """
    This function tests '/' route of the application without an identifier provided.
    args:
        client: pytest fixture
    return: None
    """
    route = "/"
    response = client.post(route)
    contents = json.loads(response.data)["contents"]
    assert "Success" in contents
    assert  response.status_code == 200


def test_test_identifier(client):
    """
    This function tests '/test' route of the application with an identifier provided.
    args:
        client: pytest fixture
    return: None
    """
    route = "/test"
    response = client.post(route, data=__prepare_payload())
    contents = json.loads(response.data)["contents"]
    assert "Success" in contents
    assert response.status_code == 200


def test_test_without_identifier(client):
    """
    This function tests '/test' route of the application without an identifier provided.
    args:
        client: pytest fixture
    return: None
    """
    route = "/test"
    response = client.post(route)
    contents = json.loads(response.data)["contents"]
    assert "Success" in contents
    assert response.status_code == 200
