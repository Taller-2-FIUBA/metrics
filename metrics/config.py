"""Application configuration."""
from environ import bool_var, config, var, group


@config(prefix="METRICS")
class AppConfig:
    """Application configuration values from environment."""

    log_level = var("INFO")

    @config(prefix="MONGO")
    class Mongo:
        """MongoDB configuration."""

        enabled = bool_var(True)
        driver = var("mongodb")
        user = var("fiufit")
        password = var("fiufit")
        host = var("cluster.mongodb.net")
        database = var("fiufit")

    @config(prefix="REDIS")
    class Redis:
        """Redis configuration."""

        host = var("localhost")
        port = var(6379, converter=int)

    mongo = group(Mongo)  # type: ignore
    redis = group(Redis)  # type: ignore
