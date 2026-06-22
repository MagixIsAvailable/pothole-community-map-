"""API v1 router — aggregates all endpoint modules."""

from fastapi import APIRouter

from api.app.api.v1 import health, uploads, detections, events, map, reviews

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(uploads.router, prefix="/uploads", tags=["uploads"])
api_router.include_router(detections.router, prefix="/detections", tags=["detections"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(map.router, prefix="/map", tags=["map"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
