"""Requests handlers."""
import logging
import time
from typing import List

from fastapi import FastAPI, Request
from fastapi.applications import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware

import metrics.constants as c
from metrics.dto import MetricDto
from metrics.healthcheck import HealthCheckDto
from metrics.hydrator import hydrate
from metrics.mongodb import get_url, get_connection, get_values


logging.basicConfig(encoding="utf-8", level=c.CONFIGURATION.log_level.upper())
app = FastAPI(
    debug=c.CONFIGURATION.log_level.upper() == "DEBUG",
    openapi_url=c.DOCUMENTATION_URI + "openapi.json",
)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=c.ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=c.METHODS,
    allow_headers=['*']
)


@app.get(c.BASE_URI, response_model=List[MetricDto])
async def get_metric(name: str) -> List[MetricDto]:
    """Get value for a metric name."""
    logging.info("Returning value for metric %s", name)
    connection = get_connection(get_url(c.CONFIGURATION))
    values = get_values(connection, name)
    logging.debug("Got %s for %s", values, name)
    return hydrate(values)


@app.get(c.DOCUMENTATION_URI, include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    """To show Swagger with API documentation."""
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="FIU-FIT Metrics",
    )


@app.get(c.BASE_URI + "/healthcheck/")
async def health_check() -> HealthCheckDto:
    """Check for how long has the service been running."""
    return HealthCheckDto(uptime=time.time() - c.START)
