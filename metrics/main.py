"""Requests handlers."""
import logging
import time

from fastapi import FastAPI, Request
from fastapi.applications import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware

import metrics.constants as c
from metrics.healthcheck import HealthCheckDto


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


@app.get("/")
async def root():
    """Greet."""
    logging.info("Received request to /")
    return {"message": "Hello World"}


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
