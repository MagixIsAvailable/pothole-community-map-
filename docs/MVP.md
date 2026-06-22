# MVP Scope — Pothole Community Map

## Goal

A locally runnable system that lets a community member upload a photo/video of
a road surface, automatically detects potholes via a YOLOv8 model, and displays
the results on an interactive map so other users can review and track repair
status.

## What's In Scope (v1)

### 1. Upload & Detect
- Accept image / short video via a browser upload form.
- Run YOLOv8n inference (CPU-first, single-class `pothole`).
- Return bounding boxes + confidence scores as JSON.

### 2. Geotag & Cluster
- Extract GPS from EXIF or accept manual lat/lng input.
- Cluster nearby detections that may represent the same pothole using DBSCAN.

### 3. Interactive Map
- Leaflet map showing pothole points as GeoJSON markers.
- Colour-coded by status and severity.
- Filters: status, date range, confidence threshold.

### 4. Review Workflow
- Status lifecycle: `detected` → `under_review` → `confirmed | rejected` → `repaired`.
- Simple review page to accept/reject/repair a pothole event.
- Upvote/vote-to-fix placeholder (no auth yet).

### 5. Data Export
- Export filtered events as GeoJSON / CSV.
- Serve GeoJSON endpoint for map consumption.

## What's Out of Scope (v1)
- User authentication / roles.
- Council / municipality API integration.
- Real-time video streaming.
- Mobile app.
- PostGIS — single-node SQLite only.
- 3D visualisation.
- Multi-class detection (cracks, patches, etc.).

## Tech Stack (v1)
| Layer       | Choice                        |
|-------------|-------------------------------|
| ML          | Python 3.11+, Ultralytics YOLOv8 |
| API         | FastAPI (Python)              |
| Web         | React 18 + Vite + TypeScript  |
| Map         | Leaflet + react-leaflet       |
| DB          | SQLite (SQLAlchemy ORM)       |
| Geo format  | GeoJSON (RFC 7946)            |
| Task queue  | Lightweight in-process queue (ARQ later) |

## Success Criteria
- [ ] Upload a photo → get detection result with bbox within 3 s (local CPU).
- [ ] Map loads with sample pothole points from API.
- [ ] Review page changes pothole status and persists to DB.
- [ ] Run `scripts/bootstrap.sh` and have API + web running on `localhost`.
