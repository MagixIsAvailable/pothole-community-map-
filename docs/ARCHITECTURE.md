# Architecture — Pothole Community Map

## High-Level Overview

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   web/       │────▶│   api/       │────▶│   ml/        │
│  React+Vite  │     │  FastAPI     │     │  YOLOv8      │
│  Leaflet     │     │  SQLAlchemy  │     │  scripts/src │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                     ┌──────▼───────┐
                     │   SQLite DB  │
                     └──────────────┘
```

## Layer Responsibilities

### `web/` — Presentation Layer
- React 18 SPA with Vite bundler.
- Routes: Home, Map, Upload, Review, About.
- Communicates with API exclusively via REST + JSON.
- Leaflet renders GeoJSON layers returned by API.

### `api/` — Application Layer
- FastAPI app serving REST endpoints under `/api/v1/`.
- **Routers** (`api/v1/`): Thin HTTP handlers — parse, validate, delegate.
- **Services** (`services/`): Business logic — detection orchestration, clustering, geotagging.
- **Repositories** (`repositories/`): Data access — one repo per aggregate.
- **Schemas** (`schemas/`): Pydantic models for request/response serialisation.
- **DB Models** (`db/models/`): SQLAlchemy ORM models.
- **Workers** (`workers/`): Async task queue (in-process for MVP).

### `ml/` — Machine Learning Layer
- **src/**: Reusable library — dataset loading, transforms, training loop, inference helpers.
- **scripts/**: Runnable entry points — train, evaluate, infer_images, infer_video, geotag, export_geojson.
- **notebooks/**: Exploratory & documented workflows mirroring scripts.
- **configs/**: YAML config files for training/inference runs.
- **models/**: Saved weights and checkpoints (gitignored).

## Data Flow — Upload → Map

```
User uploads photo/video
        │
        ▼
  POST /api/v1/uploads
        │
        ▼
  upload_service.py          ← save file, extract EXIF GPS
        │
        ▼
  detection_service.py       ← run YOLO inference
        │
        ▼
  geotag_service.py          ← attach lat/lng to detections
        │
        ▼
  clustering_service.py      ← DBSCAN nearby detections → events
        │
        ▼
  event_service.py           ← create/update pothole_events
        │
        ▼
  GET /api/v1/map/geojson    ← serve GeoJSON FeatureCollection
        │
        ▼
  MapView.tsx (Leaflet)      ← render markers on map
```

## Database Design (SQLite)

See `docs/DATA_SCHEMA.md` for full schema.

### Core Tables
- `media` — uploaded images/videos
- `detections` — individual YOLO bounding boxes
- `pothole_events` — clustered, deduplicated pothole entities
- `reviews` — user review actions on events

## Key Design Decisions (see `docs/DECISIONS.md`)
- SQLite for local dev; schema designed for easy Postgres/PostGIS migration.
- Single `pothole` class for v1; extendable via `class_id` field.
- GeoJSON as wire format for map layer — no GeoDjango or PostGIS required for MVP.
- In-process task queue; replace with ARQ/Celery when needed.
