"""MongoDB connection and queries."""
import logging

from pymongo import MongoClient

from metrics.config import AppConfig


def get_mongo_url(config: AppConfig) -> str:
    """Build MongoDB URI."""
    return f"{config.mongo.driver}://{config.mongo.user}:" +\
        f"{config.mongo.password}@{config.mongo.host}/{config.mongo.database}"


def get_mongodb_connection(connection_string: str) -> MongoClient:
    """Create a MongoDB connection."""
    logging.debug("Connecting to mongo db using %s", connection_string)
    client = MongoClient(connection_string)
    return client
