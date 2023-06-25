# pylint: disable= missing-module-docstring, missing-function-docstring
from fastapi.testclient import TestClient
from hamcrest import assert_that, greater_than
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


def test_when_checking_healthcheck_expect_uptime_greater_than_zero():
    response = client.get("metrics/healthcheck/")
    assert response.status_code == 200, response.json()
    assert_that(response.json()["uptime"], greater_than(0))
