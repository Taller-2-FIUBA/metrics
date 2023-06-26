"""Worker."""
import logging

import click

from redis import ConnectionPool, Redis

import metrics.constants as c

logging.basicConfig(
    encoding="utf-8",
    level=c.CONFIGURATION.log_level.upper(),
    format="%(message)s"
)

@click.command()
def read():
    """Read metrics from Reddis."""
    logging.info("Connecting to Reddis...")
    pool = ConnectionPool(
        host=c.CONFIGURATION.redis.host,
        port=c.CONFIGURATION.redis.port,
        db=0,
    )
    client = Redis(connection_pool=pool)
    logging.info("Reading metrics...")
    while True:
        metric = client.blpop("metrics")
        logging.info("Read %s", metric)


if __name__ == '__main__':
    read()
