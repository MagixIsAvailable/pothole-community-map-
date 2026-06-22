"""SQLAlchemy model for users (placeholder for future auth)."""

from datetime import datetime, timezone

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from api.app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    display_name: Mapped[str] = mapped_column(String(128), default="anonymous")
    created_at: Mapped[str] = mapped_column(
        String(64), default=lambda: datetime.now(timezone.utc).isoformat()
    )
