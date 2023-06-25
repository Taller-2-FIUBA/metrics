# pylint: disable= missing-module-docstring, missing-function-docstring
from os import environ
from unittest.mock import patch
from environ import to_config
from metrics.config import AppConfig


@patch.dict(environ, {}, clear=True)
def test_when_environment_is_empty_expect_warning_log_level():
    cnf = to_config(AppConfig)
    assert cnf.log_level == "WARNING"


@patch.dict(environ, {"METRICS_LOG_LEVEL": "DEBUG"}, clear=True)
def test_when_environment_debug_log_level_expect_debug():
    cnf = to_config(AppConfig)
    assert cnf.log_level == "DEBUG"


@patch.dict(environ, clear=True)
def test_when_mongo_enabled_env_variable_is_not_set_expect_true():
    cnf = to_config(AppConfig)
    assert cnf.mongo.enabled


@patch.dict(environ, {"METRICS_MONGO_ENABLED": "False"}, clear=True)
def test_when_mongo_enabled_env_variable_is_false_expect_false():
    cnf = to_config(AppConfig)
    assert not cnf.mongo.enabled


@patch.dict(environ, clear=True)
def test_when_environment_mongo_driver_expect_mongodb():
    cnf = to_config(AppConfig)
    assert cnf.mongo.driver == "mongodb"


@patch.dict(environ, {"METRICS_MONGO_DRIVER": "mongodb+srv"}, clear=True)
def test_when_environment_mongo_driver_expect_mongodb_srv():
    cnf = to_config(AppConfig)
    assert cnf.mongo.driver == "mongodb+srv"


@patch.dict(environ, clear=True)
def test_when_environment_mongo_user_expect_fiufit():
    cnf = to_config(AppConfig)
    assert cnf.mongo.user == "fiufit"


@patch.dict(environ, {"METRICS_MONGO_USER": "fiufitmongo"}, clear=True)
def test_when_environment_mongo_user_expect_fiufitmongo():
    cnf = to_config(AppConfig)
    assert cnf.mongo.user == "fiufitmongo"


@patch.dict(environ, clear=True)
def test_when_environment_mongo_password_expect_fiufit():
    cnf = to_config(AppConfig)
    assert cnf.mongo.password == "fiufit"


@patch.dict(environ, {"METRICS_MONGO_PASSWORD": "secure"}, clear=True)
def test_when_environment_mongo_password_expect_secure():
    cnf = to_config(AppConfig)
    assert cnf.mongo.password == "secure"


@patch.dict(environ, clear=True)
def test_when_environment_mongo_host_expect_cluster_mongodb_net():
    cnf = to_config(AppConfig)
    assert cnf.mongo.host == "cluster.mongodb.net"


@patch.dict(environ, {"METRICS_MONGO_HOST": "mongodb-release"}, clear=True)
def test_when_environment_mongo_host_expect_mongodb_release():
    cnf = to_config(AppConfig)
    assert cnf.mongo.host == "mongodb-release"


@patch.dict(environ, clear=True)
def test_when_environment_mongo_database_expect_fiufit():
    cnf = to_config(AppConfig)
    assert cnf.mongo.database == "fiufit"


@patch.dict(environ, {"METRICS_MONGO_DATABASE": "banana"}, clear=True)
def test_when_environment_mongo_database_expect_banana():
    cnf = to_config(AppConfig)
    assert cnf.mongo.database == "banana"
