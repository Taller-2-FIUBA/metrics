"""Application constants."""

import time
from environ import to_config
from metrics.config import AppConfig

CONFIGURATION = to_config(AppConfig)
START = time.time()
BASE_URI = "/metrics"
DOCUMENTATION_URI = BASE_URI + "/documentation/"
METHODS = [
    "GET",
    "get",
    "POST",
    "post",
    "PUT",
    "put",
    "PATCH",
    "patch",
    "OPTIONS",
    "options",
    "DELETE",
    "delete",
    "HEAD",
    "head",
]
ORIGIN_REGEX = "(http)?(s)?(://)?(.*vercel.app|localhost|local)(:3000)?.*"
