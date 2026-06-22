"""Health-check endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return liveness probe."""
    return {"status": "ok", "version": "0.1.0"}
