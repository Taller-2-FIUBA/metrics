"""Worker."""
import logging
from json import loads

import click
from redis import BlockingConnectionPool, Redis

import metrics.constants as c
from metrics.mongodb import get_connection, get_url, add

logging.basicConfig(
    encoding="utf-8",
    level=c.CONFIGURATION.log_level.upper(),
    format="%(message)s"
)


@click.command()
@click.option('--read-one', default=False)
def read(read_one: bool):
    """Read metrics from Reddis."""
    logging.info("Connecting to Reddis...")
    pool = BlockingConnectionPool(
        host=c.CONFIGURATION.redis.host,
        port=c.CONFIGURATION.redis.port,
        db=0,
        timeout=10,
    )
    client = Redis(connection_pool=pool)
    logging.info("Connecting to MongoDB...")
    connection = get_connection(get_url(c.CONFIGURATION))
    logging.info("Reading metrics...")
    should_read_more = True
    while should_read_more:
        logging.debug("Reading metric from Reddis...")
        message = client.blpop("metrics")
        logging.info("Read message %s", message)
        try:
            sanitized_message = message[1].decode('utf-8').replace("'", '"')
            logging.debug("Sanitized message %s", sanitized_message)
            add(connection, loads(sanitized_message))
            logging.debug("Saved metric in MongoDB.")
        except (SyntaxError, IndexError):
            logging.exception("Cloud not save metric.")
        if read_one:
            logging.info("Configured to read one message, existing...")
            should_read_more = False


# pylint: disable=no-value-for-parameter
if __name__ == '__main__':
    read()
