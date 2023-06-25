"""Requests handlers."""
import logging

from fastapi import FastAPI
from environ import to_config
from metrics.config import AppConfig


CONFIGURATION = to_config(AppConfig)
app = FastAPI(debug=CONFIGURATION.log_level.upper() == "DEBUG")
logging.basicConfig(encoding="utf-8", level=CONFIGURATION.log_level.upper())


@app.get("/")
async def root():
    """Greet."""
    logging.info("Received request to /")
    return {"message": "Hello World"}
