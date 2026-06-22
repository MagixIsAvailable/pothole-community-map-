"""DBSCAN clustering for deduplicating pothole detections."""

from typing import Any

import numpy as np
from sklearn.cluster import DBSCAN


def latlng_to_radians(lat: float, lng: float) -> tuple[float, float]:
    """Convert lat/lng degrees to approximate metres using a simple equatorial approximation."""
    lat_rad = np.radians(lat)
    # 1 degree latitude ≈ 111,320 m
    # 1 degree longitude ≈ 111,320 * cos(lat) m
    return lat * 111_320, lng * 111_320 * np.cos(lat_rad)


def cluster_detections_dbscan(
    detections: list[dict[str, Any]],
    eps_meters: float = 15.0,
    min_samples: int = 2,
) -> list[dict[str, Any]]:
    """Group nearby detections into pothole events using DBSCAN.

    Args:
        detections: List of detection dicts with 'lat' and 'lng'.
        eps_meters: Maximum distance (metres) between points in a cluster.
        min_samples: Minimum detections to form a cluster.

    Returns:
        Detections list with 'cluster_id' appended.
    """
    if len(detections) < 2:
        for i, det in enumerate(detections):
            det["cluster_id"] = i
        return detections

    coords = np.array([
        latlng_to_radians(d["lat"], d["lng"]) for d in detections
    ])

    clustering = DBSCAN(eps=eps_meters, min_samples=min_samples, metric="euclidean").fit(coords)

    for i, label in enumerate(clustering.labels_):
        detections[i]["cluster_id"] = int(label)  # -1 = noise

    return detections
