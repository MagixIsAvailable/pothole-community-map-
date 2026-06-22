"""SQLAlchemy model for individual detections."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.app.db.base import Base


class Detection(Base):
    __tablename__ = "detections"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    media_id: Mapped[str] = mapped_column(String(36), ForeignKey("media.id"), nullable=False)
    class_id: Mapped[int] = mapped_column(Integer, default=0)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    x_center: Mapped[float] = mapped_column(Float, nullable=False)
    y_center: Mapped[float] = mapped_column(Float, nullable=False)
    width: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    frame_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[str] = mapped_column(
        String(64), default=lambda: datetime.now(timezone.utc).isoformat()
    )
