"""Database session dependency for FastAPI."""

from collections.abc import Generator

from sqlalchemy.orm import Session

from api.app.db.base import get_engine

_engine = get_engine()


def get_session() -> Generator[Session, None, None]:
    """Yield a new SQLAlchemy session per request."""
    with Session(_engine) as session:
        yield session
