"""Events endpoints — CRUD for pothole events."""

from fastapi import APIRouter

router = APIRouter()


# TODO: Wire to event_service + events_repo when DB models are in place.
@router.get("")
async def list_events() -> list[dict]:
    """List all pothole events (placeholder)."""
    return []
