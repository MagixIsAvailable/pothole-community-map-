"""Pydantic schemas for pothole events."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PotholeEventBase(BaseModel):
    lat: float
    lng: float
    severity: str = "unknown"
    status: str = "detected"


class PotholeEventCreate(PotholeEventBase):
    source_media_ids: list[str] | None = None
    detection_ids: list[str] | None = None


class PotholeEventUpdate(BaseModel):
    status: str | None = None
    severity: str | None = None
    lat: float | None = None
    lng: float | None = None


class PotholeEventRead(PotholeEventBase):
    id: UUID
    cluster_id: str | None = None
    source_media_ids: list[str] = Field(default_factory=list)
    detection_ids: list[str] = Field(default_factory=list)
    first_seen_at: datetime | None = None
    last_seen_at: datetime | None = None
    confirmed_at: datetime | None = None
    repaired_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
