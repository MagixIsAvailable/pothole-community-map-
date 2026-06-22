"""Reviews endpoints — submit and list review actions."""

from fastapi import APIRouter

router = APIRouter()


# TODO: Wire to review_service + reviews_repo when DB models are in place.
@router.get("")
async def list_reviews() -> list[dict]:
    """List all reviews (placeholder)."""
    return []
