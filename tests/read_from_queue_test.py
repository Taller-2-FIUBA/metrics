# pylint: disable= missing-module-docstring, missing-function-docstring
from unittest.mock import MagicMock, patch
from click.testing import CliRunner
from metrics.read_from_queue import read

expected_message = (
    bytes("metrics", "utf-8"),
    bytes('{"metric": "trainings_created_count", "value": 1, "label": "Arm",\
    "date": "2023-06-24T23:26:45-03:00"}', "utf-8")
)


@patch("metrics.read_from_queue.BlockingConnectionPool")
@patch("metrics.read_from_queue.Redis")
@patch("metrics.read_from_queue.get_connection")
@patch("metrics.read_from_queue.add")
def test_when_creating_connection_pool_expect_parameters(
    add_mock: MagicMock,
    get_connection_mock: MagicMock,
    redis_mock: MagicMock,
    blocking_connection_pool_mock: MagicMock,
):
    expected_client = MagicMock()
    expected_client.blpop.return_value = expected_message
    redis_mock.return_value = expected_client
    runner = CliRunner()
    runner.invoke(read, ["--read-one=True"])
    add_mock.assert_called_once()
    get_connection_mock.assert_called_once()
    redis_mock.assert_called_once()
    blocking_connection_pool_mock.assert_called_once_with(
        host='localhost', port=6379, db=0, timeout=10
    )


@patch("metrics.read_from_queue.BlockingConnectionPool")
@patch("metrics.read_from_queue.Redis")
@patch("metrics.read_from_queue.get_connection")
@patch("metrics.read_from_queue.add")
def test_when_creating_redis_instance_expect_pool(
    add_mock: MagicMock,
    get_connection_mock: MagicMock,
    redis_mock: MagicMock,
    blocking_connection_pool_mock: MagicMock,
):
    expected_pool = MagicMock()
    blocking_connection_pool_mock.return_value = expected_pool
    expected_client = MagicMock()
    expected_client.blpop.return_value = expected_message
    redis_mock.return_value = expected_client
    runner = CliRunner()
    runner.invoke(read, ["--read-one=True"])
    add_mock.assert_called_once()
    get_connection_mock.assert_called_once()
    redis_mock.assert_called_once_with(connection_pool=expected_pool)
    blocking_connection_pool_mock.assert_called_once()


@patch("metrics.read_from_queue.BlockingConnectionPool")
@patch("metrics.read_from_queue.Redis")
@patch("metrics.read_from_queue.get_connection")
@patch("metrics.read_from_queue.add")
def test_when_getting_mongodb_connection_expect_string(
    add_mock: MagicMock,
    get_connection_mock: MagicMock,
    redis_mock: MagicMock,
    blocking_connection_pool_mock: MagicMock,
):
    expected_client = MagicMock()
    expected_client.blpop.return_value = expected_message
    redis_mock.return_value = expected_client
    runner = CliRunner()
    runner.invoke(read, ["--read-one=True"])
    add_mock.assert_called_once()
    get_connection_mock.assert_called_once_with(
        "mongodb://fiufit:fiufit@cluster.mongodb.net/fiufit"
    )
    redis_mock.assert_called_once()
    blocking_connection_pool_mock.assert_called_once()


@patch("metrics.read_from_queue.BlockingConnectionPool")
@patch("metrics.read_from_queue.Redis")
@patch("metrics.read_from_queue.get_connection")
@patch("metrics.read_from_queue.add")
def test_when_saving_message_expect_metrics(
    add_mock: MagicMock,
    get_connection_mock: MagicMock,
    redis_mock: MagicMock,
    blocking_connection_pool_mock: MagicMock,
):
    expected_client = MagicMock()
    expected_client.blpop.return_value = expected_message
    expected_connection = MagicMock()
    redis_mock.return_value = expected_client
    get_connection_mock.return_value = expected_connection
    runner = CliRunner()
    runner.invoke(read, ["--read-one=True"])
    blocking_connection_pool_mock.assert_called_once()
    add_mock.assert_called_once_with(
        expected_connection,
        {
            "metric": "trainings_created_count",
            "value": 1,
            "label": "Arm",
            "date": "2023-06-24T23:26:45-03:00"
        },
    )


@patch("metrics.read_from_queue.BlockingConnectionPool")
@patch("metrics.read_from_queue.Redis")
@patch("metrics.read_from_queue.get_connection")
@patch("metrics.read_from_queue.add")
def test_when_message_is_invalid_expect_no_call(
    add_mock: MagicMock,
    get_connection_mock: MagicMock,
    redis_mock: MagicMock,
    blocking_connection_pool_mock: MagicMock,
):
    expected_pool = MagicMock()
    blocking_connection_pool_mock.return_value = expected_pool
    expected_client = MagicMock()
    expected_client.blpop.return_value = ("", bytes("{'a}", "utf-8"))
    redis_mock.return_value = expected_client
    runner = CliRunner()
    runner.invoke(read, ["--read-one=True"])
    add_mock.assert_not_called()
    get_connection_mock.assert_called_once()
    redis_mock.assert_called_once_with(connection_pool=expected_pool)
    blocking_connection_pool_mock.assert_called_once()
