"""Detections endpoints — list and query individual detection records."""

from fastapi import APIRouter

router = APIRouter()


# TODO: Wire to detection_service + detections_repo when DB models are in place.
@router.get("")
async def list_detections() -> list[dict]:
    """List all detections (placeholder)."""
    return []
