"""Requests handlers."""
import logging

from fastapi import FastAPI, Request
from fastapi.applications import get_swagger_ui_html

import metrics.constants as c


app = FastAPI(
    debug=c.CONFIGURATION.log_level.upper() == "DEBUG",
    openapi_url=c.DOCUMENTATION_URI + "openapi.json",
)
logging.basicConfig(encoding="utf-8", level=c.CONFIGURATION.log_level.upper())


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
