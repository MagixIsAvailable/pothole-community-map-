#!/usr/bin/env python
"""Deduplicate pothole detections into unified events using DBSCAN clustering.

Usage:
    python ml/scripts/deduplicate_events.py --detections data/exports/csv/detections.csv --output data/exports/geojson/
"""

import argparse


def main(detections_path: str, output: str, eps_meters: float, min_samples: int) -> None:
    """Cluster nearby detections and produce deduplicated pothole events."""
    # TODO: Implement DBSCAN clustering on lat/lng.
    # TODO: Output clustered events as GeoJSON.
    print(f"Clustering detections from {detections_path} → {output}")
    print(f"  eps={eps_meters}m, min_samples={min_samples}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deduplicate pothole detections")
    parser.add_argument("--detections", required=True)
    parser.add_argument("--output", default="data/exports/geojson/")
    parser.add_argument("--eps-meters", type=float, default=15.0)
    parser.add_argument("--min-samples", type=int, default=2)
    args = parser.parse_args()
    main(args.detections, args.output, args.eps_meters, args.min_samples)
