"""Pydantic schemas for upload responses (re-exports from media)."""

from api.app.schemas.media import DetectionResult, UploadResponse

__all__ = ["DetectionResult", "UploadResponse"]
