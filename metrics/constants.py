"""Application constants."""

from environ import to_config
from metrics.config import AppConfig

CONFIGURATION = to_config(AppConfig)
BASE_URI = "/metrics"
DOCUMENTATION_URI = BASE_URI + "/documentation/"
