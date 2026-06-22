"""SQLAlchemy model for deduplicated pothole events."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column

from api.app.db.base import Base


class PotholeEvent(Base):
    __tablename__ = "pothole_events"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    lng: Mapped[float] = mapped_column(Float, nullable=False)
    severity: Mapped[str] = mapped_column(String(16), default="unknown")  # low, medium, high, unknown
    status: Mapped[str] = mapped_column(String(32), default="detected")  # detected, under_review, confirmed, rejected, repaired
    cluster_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    source_media_ids: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON array
    detection_ids: Mapped[str | None] = mapped_column(Text, nullable=True)   # JSON array
    first_seen_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    last_seen_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    confirmed_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    repaired_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    created_at: Mapped[str] = mapped_column(
        String(64), default=lambda: datetime.now(timezone.utc).isoformat()
    )
    updated_at: Mapped[str] = mapped_column(
        String(64),
        default=lambda: datetime.now(timezone.utc).isoformat(),
        onupdate=lambda: datetime.now(timezone.utc).isoformat(),
    )
