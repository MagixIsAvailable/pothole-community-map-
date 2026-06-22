"""SQLAlchemy declarative base and engine helpers."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from api.app.core.config import get_settings


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass


def get_engine():
    """Create a SQLAlchemy engine from settings."""
    settings = get_settings()
    connect_args = {}
    if settings.DATABASE_URL.startswith("sqlite"):
        connect_args["check_same_thread"] = False
    return create_engine(settings.DATABASE_URL, echo=settings.DEBUG, connect_args=connect_args)


def init_db() -> None:
    """Create all tables if they don't exist."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
