"""Map endpoint — serve GeoJSON for Leaflet map layer."""

import uuid
from typing import Any

from fastapi import APIRouter, Query

router = APIRouter()


def _sample_geojson() -> dict[str, Any]:
    """Generate sample GeoJSON FeatureCollection for MVP map rendering."""
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [-2.11, 57.15]},
                "properties": {
                    "id": str(uuid.uuid4()),
                    "status": "confirmed",
                    "severity": "high",
                    "detection_count": 5,
                    "first_seen": "2026-06-01T10:00:00Z",
                    "last_seen": "2026-06-20T14:30:00Z",
                },
            },
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [-2.09, 57.16]},
                "properties": {
                    "id": str(uuid.uuid4()),
                    "status": "under_review",
                    "severity": "medium",
                    "detection_count": 2,
                    "first_seen": "2026-06-10T08:15:00Z",
                    "last_seen": "2026-06-18T09:45:00Z",
                },
            },
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [-2.13, 57.14]},
                "properties": {
                    "id": str(uuid.uuid4()),
                    "status": "detected",
                    "severity": "low",
                    "detection_count": 1,
                    "first_seen": "2026-06-19T16:20:00Z",
                    "last_seen": "2026-06-19T16:20:00Z",
                },
            },
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [-2.10, 57.17]},
                "properties": {
                    "id": str(uuid.uuid4()),
                    "status": "repaired",
                    "severity": "medium",
                    "detection_count": 3,
                    "first_seen": "2026-05-15T07:00:00Z",
                    "last_seen": "2026-06-05T11:00:00Z",
                },
            },
        ],
    }


@router.get("/geojson")
async def get_geojson(
    status: str | None = Query(None, description="Filter by status"),
    min_confidence: float | None = Query(None, ge=0.0, le=1.0),
) -> dict[str, Any]:
    """Return pothole events as a GeoJSON FeatureCollection."""
    geojson = _sample_geojson()

    # Apply status filter to sample data
    if status:
        geojson["features"] = [
            f
            for f in geojson["features"]
            if f["properties"]["status"] == status
        ]

    return geojson
