# pylint: disable=no-name-in-module
"""DTOs."""
from pydantic import BaseModel


class MetricDto(BaseModel):
    """Metrics response model."""

    label: str
    count: int
