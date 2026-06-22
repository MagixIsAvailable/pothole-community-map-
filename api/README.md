# API — Pothole Community Map

FastAPI backend serving REST endpoints for upload, detection, map data, and reviews.

## Quick Start

```bash
cd api
pip install -e ..[dev]
uvicorn api.app.main:app --reload --host 127.0.0.1 --port 8000
```

## API Documentation

When running locally with `DEBUG=true`, interactive docs are available at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method   | Path                    | Description                       |
|----------|-------------------------|-----------------------------------|
| `GET`    | `/api/v1/health`        | Liveness check                    |
| `POST`   | `/api/v1/uploads`       | Upload image/video for detection  |
| `GET`    | `/api/v1/detections`    | List individual detections        |
| `GET`    | `/api/v1/events`        | List pothole events               |
| `GET`    | `/api/v1/map/geojson`   | GeoJSON FeatureCollection for map |
| `GET`    | `/api/v1/reviews`       | List review actions               |
| `POST`   | `/api/v1/reviews`       | Submit a review action            |

## Architecture

```
api/app/
├── main.py           # FastAPI app creation + lifespan
├── core/             # Config, logging, security
├── db/               # SQLAlchemy base, session, models
├── schemas/          # Pydantic request/response models
├── api/v1/           # Route handlers (thin)
├── services/         # Business logic
├── repositories/     # Data access layer
└── workers/          # Async task queue (in-process for MVP)
```
