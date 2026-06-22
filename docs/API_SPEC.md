# API Specification — Pothole Community Map

Base URL: `http://127.0.0.1:8000/api/v1`

## Health

### `GET /health`
Returns liveness status.

**Response 200:**
```json
{ "status": "ok", "version": "0.1.0" }
```

## Uploads

### `POST /uploads`
Upload an image or video for pothole detection.

**Request:** `multipart/form-data`
| Field | Type    | Required | Description              |
|-------|---------|----------|--------------------------|
| file  | binary  | yes      | Image or video file      |
| lat   | float   | no       | Manual latitude override |
| lng   | float   | no       | Manual longitude override|

**Response 200:**
```json
{
  "media_id": "uuid",
  "filename": "pothole.jpg",
  "filepath": "/storage/uploads/abc123.jpg",
  "media_type": "image",
  "lat": 51.5074,
  "lng": -0.1278,
  "detections": [
    {
      "id": "uuid",
      "media_id": "uuid",
      "class_id": 0,
      "class_name": "pothole",
      "confidence": 0.87,
      "x_center": 0.45,
      "y_center": 0.60,
      "width": 0.12,
      "height": 0.08
    }
  ]
}
```

## Map

### `GET /map/geojson`
Return pothole events as GeoJSON FeatureCollection.

**Query Parameters:**
| Param          | Type   | Description                  |
|----------------|--------|------------------------------|
| status         | string | Filter by event status       |
| min_confidence | float  | Minimum detection confidence |

**Response 200:**
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [-0.1278, 51.5074] },
      "properties": {
        "id": "uuid",
        "status": "confirmed",
        "severity": "high",
        "detection_count": 5,
        "first_seen": "2026-06-01T10:00:00Z",
        "last_seen": "2026-06-20T14:30:00Z"
      }
    }
  ]
}
```

## Events

### `GET /events`
List all pothole events.

### `PATCH /events/{id}`
Update a pothole event status or severity.

## Reviews

### `GET /reviews`
List review actions.

### `POST /reviews`
Submit a review action.

**Request body:**
```json
{
  "event_id": "uuid",
  "action": "confirm",
  "comment": "Verified on site"
}
```

## Detections

### `GET /detections`
List individual YOLO detection records.

## Status Values
| Status         | Description                              |
|----------------|------------------------------------------|
| detected       | Auto-detected by model, not yet reviewed |
| under_review   | Being reviewed by a community member     |
| confirmed      | Verified as a real pothole               |
| rejected       | False positive, dismissed                |
| repaired       | Pothole has been filled                  |
