#!/usr/bin/env python
"""Export pothole events as GeoJSON for map consumption.

Usage:
    python ml/scripts/export_geojson.py --events data/exports/csv/events.csv --output data/exports/geojson/
"""

import argparse
import json
from pathlib import Path


def main(events_path: str, output: str) -> None:
    """Convert pothole events to RFC 7946 GeoJSON FeatureCollection."""
    # TODO: Read pothole_events from DB or CSV and convert to GeoJSON.
    output_file = Path(output) / "potholes.geojson"
    geojson = {"type": "FeatureCollection", "features": []}
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(geojson, indent=2))
    print(f"GeoJSON written to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export pothole events as GeoJSON")
    parser.add_argument("--events", required=True)
    parser.add_argument("--output", default="data/exports/geojson/")
    args = parser.parse_args()
    main(args.events, args.output)
