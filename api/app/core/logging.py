"""Centralised logging configuration."""

import logging
import sys


def setup_logging(debug: bool = False) -> None:
    """Configure root logger with consistent formatting."""
    level = logging.DEBUG if debug else logging.INFO
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    logging.basicConfig(level=level, format=fmt, stream=sys.stdout)

    # Silence noisy third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("PIL").setLevel(logging.WARNING)
