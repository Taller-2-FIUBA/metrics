# pylint: disable= missing-module-docstring, missing-function-docstring
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from hamcrest import assert_that, greater_than
from metrics.main import app

import tests.util.constants as c

client = TestClient(app)


@patch("metrics.main.get_connection")
@patch("metrics.main.get_values")
def test_get_metric(
    get_values_mock: MagicMock,
    get_connection_mock: MagicMock,
):
    expected_values = [{"_id": "arm", "count": 33}, {"_id": "leg", "count": 3}]
    expected_connection = MagicMock()
    get_values_mock.return_value = expected_values
    get_connection_mock.return_value = expected_connection
    response = client.get("/metrics?name=trainings_created_count")
    assert response.status_code == 200
    assert response.json() == [
        {"label": "arm", "count": 33}, {"label": "leg", "count": 3}
    ]
    get_connection_mock.assert_called_once_with(
        "mongodb://fiufit:fiufit@cluster.mongodb.net/fiufit"
    )
    get_values_mock.assert_called_once_with(
        expected_connection, "trainings_created_count"
    )


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


def test_when_asking_cors_is_available_for_patch_expect_200():
    response = client.options("metrics", headers=c.HEADERS)
    assert response.status_code == 200


def test_when_asking_cors_is_available_for_patch_uppercase_expect_200():
    method_override = {"access-control-request-method": "PATCH"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_for_post_expect_200():
    method_override = {"access-control-request-method": "post"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_for_post_uppercase_expect_200():
    method_override = {"access-control-request-method": "POST"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_for_banana_expect_400():
    method_override = {"access-control-request-method": "banana"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 400


def test_when_asking_cors_is_available_origin_localhost_expect_200():
    method_override = {"origin": "localhost"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_localhost_3000_expect_200():
    method_override = {"origin": "localhost:3000"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_http_localhost_expect_200():
    method_override = {"origin": "http://localhost"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_https_localhost_expect_200():
    method_override = {"origin": "https://localhost"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_http_localhost_3000_expect_200():
    method_override = {"origin": "http://localhost"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_https_localhost_3000_expect_ok():
    method_override = {"origin": "https://localhost"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_local_expect_200():
    method_override = {"origin": "local"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_local_3000_expect_200():
    method_override = {"origin": "local:3000"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_vercel_dev_expect_200():
    method_override = {"origin": "https://fiufit-backoffice.vercel.app/"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 200


def test_when_asking_cors_is_available_origin_apple_expect_200():
    method_override = {"origin": "apple"}
    response = client.options("metrics", headers=c.HEADERS | method_override)
    assert response.status_code == 400
