"""SQLAlchemy model for uploaded media."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Float, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from api.app.db.base import Base


class Media(Base):
    __tablename__ = "media"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    filename: Mapped[str] = mapped_column(String(512), nullable=False)
    filepath: Mapped[str] = mapped_column(Text, nullable=False)
    media_type: Mapped[str] = mapped_column(String(16), nullable=False)  # image / video
    mime_type: Mapped[str | None] = mapped_column(String(128), nullable=True)
    file_size: Mapped[int | None] = mapped_column(Integer, nullable=True)
    exif_lat: Mapped[float | None] = mapped_column(Float, nullable=True)
    exif_lng: Mapped[float | None] = mapped_column(Float, nullable=True)
    exif_taken_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    uploaded_at: Mapped[str] = mapped_column(
        String(64), default=lambda: datetime.now(timezone.utc).isoformat()
    )
    status: Mapped[str] = mapped_column(String(16), default="pending")
