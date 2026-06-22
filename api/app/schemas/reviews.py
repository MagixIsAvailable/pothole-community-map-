"""Pydantic schemas for reviews."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    event_id: UUID
    action: str  # confirm, reject, mark_repaired, upvote
    comment: str | None = None


class ReviewRead(BaseModel):
    id: UUID
    event_id: UUID
    action: str
    reviewer_id: str = "anonymous"
    comment: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
