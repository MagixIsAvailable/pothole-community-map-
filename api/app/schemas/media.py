"""Pydantic schemas for media uploads."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DetectionResult(BaseModel):
    """Single detection bounding box result."""
    id: str
    media_id: str
    class_id: int = 0
    class_name: str = "pothole"
    confidence: float
    x_center: float
    y_center: float
    width: float
    height: float


class UploadResponse(BaseModel):
    """Response returned after a successful upload + detection."""
    media_id: str
    filename: str | None
    filepath: str
    media_type: str
    lat: float | None = None
    lng: float | None = None
    detections: list[DetectionResult] = Field(default_factory=list)
