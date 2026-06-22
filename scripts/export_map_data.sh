#!/usr/bin/env bash
# export_map_data.sh — run geotag → cluster → export pipeline
set -euo pipefail

source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
cd "$(dirname "$0")/.."

echo "Exporting map data..."
python ml/scripts/geotag.py --media-dir storage/uploads/
python ml/scripts/deduplicate_events.py --detections data/exports/csv/detections.csv
python ml/scripts/export_geojson.py --events data/exports/csv/events.csv
echo "GeoJSON exported to data/exports/geojson/potholes.geojson"
