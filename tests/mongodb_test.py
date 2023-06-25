# pylint: disable= missing-module-docstring, missing-function-docstring
from unittest.mock import MagicMock, patch

from metrics.mongodb import (
    get_url,
    get_connection,
    get_values,
)


def test_building_url_with_config():
    config = MagicMock(**{
        "mongo.driver": "mongodb",
        "mongo.user": "fiufit",
        "mongo.password": "fiufit",
        "mongo.host": "cluster.mongodb.net",
        "mongo.database": "fiufit",
    })
    assert get_url(config) ==\
        "mongodb://fiufit:fiufit@cluster.mongodb.net/fiufit"


@patch("metrics.mongodb.MongoClient")
def test_when_creating_connection_expect_call(expected_connection: MagicMock):
    get_connection("connection_string")
    expected_connection.assert_called_once_with("connection_string")


def test_when_getting_values_expect_pipeline():
    aggregate_mock = MagicMock(return_value=[])
    connection = MagicMock(**{"fiufit.metrics.aggregate": aggregate_mock})
    expected_pipeline = [
        {"$match": {"metric": "goals_by_user_count"}},
        {"$project": {"value": 1, "label": 1, "_id": 0}},
        {
            "$addFields": {
                "label": {
                    "$cond": [
                        {"$eq": [{"$ifNull": ["$label", 0]}, 0]},
                        "total",
                        "$label"
                    ]
                }
            }
        },
        {"$group": {"_id": "$label", "count": {"$sum": "$value"}}}
    ]
    assert not get_values(connection, "goals_by_user_count")
    aggregate_mock.assert_called_once_with(expected_pipeline)
