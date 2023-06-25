"""Application constants."""

import time
from environ import to_config
from metrics.config import AppConfig

CONFIGURATION = to_config(AppConfig)
START = time.time()
BASE_URI = "/metrics"
DOCUMENTATION_URI = BASE_URI + "/documentation/"
