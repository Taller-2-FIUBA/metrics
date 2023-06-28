"""MongoDB connection and queries."""
import logging
from typing import Dict, List

from pymongo import MongoClient

from metrics.config import AppConfig


def get_url(config: AppConfig) -> str:
    """Build MongoDB URI."""
    return f"{config.mongo.driver}://{config.mongo.user}:" +\
        f"{config.mongo.password}@{config.mongo.host}/{config.mongo.database}"


def get_connection(connection_string: str) -> MongoClient:
    """Create a MongoDB connection."""
    logging.debug("Connecting to mongo db using %s", connection_string)
    client = MongoClient(connection_string)
    return client


def get_values(connection: MongoClient, name: str) -> List[Dict]:
    """Return values for a metric name."""
    logging.info("Reading metric values...")
    pipeline = [
        {
            "$match": {
                "metric": name
            }
        }, {
            "$project": {
                "value": 1,
                "label": 1,
                "_id": 0
            }
        }, {
            "$addFields": {
                "label": {
                    "$cond": [
                        {
                            "$eq": [
                                {
                                    "$ifNull": [
                                        "$label", 0
                                    ]
                                }, 0
                            ]
                        }, "total", "$label"
                    ]
                }
            }
        }, {
            "$group": {
                "_id": "$label",
                "count": {
                    "$sum": "$value"
                }
            }
        }
    ]
    return list(connection.fiufit.metrics.aggregate(pipeline))


def add(connection: MongoClient, metric: str):
    """Edit location for a user. Creates if does not exist."""
    logging.info("Saving metric %s", metric)
    connection.fiufit.metrics.insert_one(metric)
