"""SQLAlchemy model for user reviews of pothole events."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.app.db.base import Base


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id: Mapped[str] = mapped_column(String(36), ForeignKey("pothole_events.id"), nullable=False)
    action: Mapped[str] = mapped_column(String(32), nullable=False)  # confirm, reject, mark_repaired, upvote
    reviewer_id: Mapped[str] = mapped_column(String(128), default="anonymous")
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[str] = mapped_column(
        String(64), default=lambda: datetime.now(timezone.utc).isoformat()
    )
