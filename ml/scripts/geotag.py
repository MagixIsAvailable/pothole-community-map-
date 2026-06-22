#!/usr/bin/env python
"""Geotag detections with GPS coordinates from EXIF or manual input.

Usage:
    python ml/scripts/geotag.py --media-dir storage/uploads/ --output data/exports/geojson/
"""

import argparse


def main(media_dir: str, output: str) -> None:
    """Extract EXIF GPS from media files and attach to detections."""
    # TODO: Use PIL.Exif or piexif to read GPS.
    # TODO: Match detections to media files and attach lat/lng.
    print(f"Geotagging media from {media_dir} → {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geotag pothole detections")
    parser.add_argument("--media-dir", required=True)
    parser.add_argument("--output", default="data/exports/geojson/")
    args = parser.parse_args()
    main(args.media_dir, args.output)
