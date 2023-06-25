# pylint: disable= missing-module-docstring, missing-function-docstring
from unittest.mock import MagicMock, patch

from metrics.mongodb import (
    get_mongo_url,
    get_mongodb_connection,
)


def test_building_url_with_config():
    config = MagicMock(**{
        "mongo.driver": "mongodb",
        "mongo.user": "fiufit",
        "mongo.password": "fiufit",
        "mongo.host": "cluster.mongodb.net",
        "mongo.database": "fiufit",
    })
    assert get_mongo_url(config) ==\
        "mongodb://fiufit:fiufit@cluster.mongodb.net/fiufit"


@patch("metrics.mongodb.MongoClient")
def test_when_creating_connection_expect_call(expected_connection: MagicMock):
    get_mongodb_connection("connection_string")
    expected_connection.assert_called_once_with("connection_string")
