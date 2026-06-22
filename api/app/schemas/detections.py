"""Pydantic schemas for detections."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class DetectionBase(BaseModel):
    media_id: UUID
    class_id: int = 0
    confidence: float
    x_center: float
    y_center: float
    width: float
    height: float
    frame_index: int | None = None


class DetectionRead(DetectionBase):
    id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}
