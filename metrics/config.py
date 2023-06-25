"""Application configuration."""
from environ import config, var, group


@config(prefix="METRICS")
class AppConfig:
    """Application configuration values from environment."""

    log_level = var("WARNING")

    @config
    class DB:
        """Database configuration."""

        driver = var("postgresql")
        password = var("backend")
        user = var("backend")
        host = var("localhost")
        port = var(5432, converter=int)
        database = var("postgres")

    db = group(DB)  # type: ignore
