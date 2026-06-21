# pothole-community-map

Community pothole detection and live mapping platform.

## MVP
- Upload road images/videos
- Run pothole detection
- Geotag and deduplicate events
- Display confirmed/filtered events on a live 2D map
- Provide counts by area, status, and severity

## Repo structure
- `ml/` model training, inference, geotagging, exports
- `api/` FastAPI backend and worker logic
- `web/` map UI and upload/review frontend
- `docs/` project scope, architecture, data schema, API spec
- `data/` raw, interim, processed datasets
