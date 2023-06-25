# pylint: disable= missing-module-docstring, missing-function-docstring
from fastapi.testclient import TestClient
from metrics.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_when_getting_swagger_ui_expect_200():
    response = client.get("metrics/documentation/")
    assert response.status_code == 200, response.json()


def test_when_getting_openapi_doc_expect_200():
    response = client.get("metrics/documentation/openapi.json")
    assert response.status_code == 200, response.json()
