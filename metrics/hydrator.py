"""Hydrate DTO from MongoDB documents."""

import logging
from typing import Dict, List
from metrics.dto import MetricDto


def hydrate(documents: List[Dict]) -> List[MetricDto]:
    """Hydrate HTTP DTOs from MongoDB documents."""
    metrics = []
    logging.info("Hydrating metrics...")
    for document in documents:
        logging.debug("Hydrating %s...", document)
        metrics.append(
            MetricDto(label=document["_id"], count=document["count"])
        )
    return metrics
