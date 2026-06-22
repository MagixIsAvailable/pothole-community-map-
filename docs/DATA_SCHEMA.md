# Data Schema — Pothole Community Map

## Entity-Relationship

```
media (1) ────< detections (N)
                    │
                    ▼
            pothole_events (1) ────< reviews (N)
```

## Tables

### `media`
Stores uploaded images or video files.

| Column       | Type      | Constraints            | Notes                        |
|-------------|-----------|------------------------|------------------------------|
| id          | UUID      | PK                     |                              |
| filename    | TEXT      | NOT NULL               | original upload filename     |
| filepath    | TEXT      | NOT NULL               | path under storage/uploads/  |
| media_type  | TEXT      | NOT NULL               | `image` or `video`           |
| mime_type   | TEXT      |                        | e.g. `image/jpeg`            |
| file_size   | INTEGER   |                        | bytes                        |
| exif_lat    | REAL      | nullable               | GPS latitude from EXIF       |
| exif_lng    | REAL      | nullable               | GPS longitude from EXIF      |
| exif_taken_at | TEXT    | nullable               | DateTimeOriginal EXIF        |
| uploaded_at | TEXT      | NOT NULL DEFAULT NOW   | server timestamp             |
| status      | TEXT      | DEFAULT 'pending'      | `pending`, `processed`, `failed` |

### `detections`
Individual bounding-box detections from YOLO inference on a media item.

| Column       | Type      | Constraints            | Notes                              |
|-------------|-----------|------------------------|------------------------------------|
| id          | UUID      | PK                     |                                    |
| media_id    | UUID      | FK → media.id          |                                    |
| class_id    | INTEGER   | DEFAULT 0              | 0 = pothole (v1 only)              |
| confidence  | REAL      | NOT NULL               | 0.0 – 1.0                         |
| x_center    | REAL      | NOT NULL               | normalised 0–1 (YOLO format)       |
| y_center    | REAL      | NOT NULL               | normalised 0–1                     |
| width       | REAL      | NOT NULL               | normalised 0–1                     |
| height      | REAL      | NOT NULL               | normalised 0–1                     |
| frame_index | INTEGER   | nullable               | for video, which frame             |
| created_at  | TEXT      | NOT NULL DEFAULT NOW   |                                    |

### `pothole_events`
Deduplicated and clustered pothole entities displayed on the map.

| Column          | Type      | Constraints            | Notes                              |
|----------------|-----------|------------------------|------------------------------------|
| id             | UUID      | PK                     |                                    |
| lat            | REAL      | NOT NULL               | representative latitude            |
| lng            | REAL      | NOT NULL               | representative longitude           |
| severity       | TEXT      | DEFAULT 'unknown'      | `low`, `medium`, `high`, `unknown` |
| status         | TEXT      | DEFAULT 'detected'     | `detected`, `under_review`, `confirmed`, `rejected`, `repaired` |
| cluster_id     | TEXT      | nullable               | DBSCAN cluster label               |
| source_media_ids | TEXT    | nullable               | JSON array of media UUIDs          |
| detection_ids  | TEXT      | nullable               | JSON array of detection UUIDs      |
| first_seen_at  | TEXT      |                        | earliest detection timestamp       |
| last_seen_at   | TEXT      |                        | latest detection timestamp         |
| confirmed_at   | TEXT      | nullable               | when status moved to confirmed     |
| repaired_at    | TEXT      | nullable               | when status moved to repaired      |
| created_at     | TEXT      | NOT NULL DEFAULT NOW   |                                    |
| updated_at     | TEXT      | NOT NULL DEFAULT NOW   |                                    |

### `reviews`
User review actions on a pothole event (no auth in v1, anonymous).

| Column       | Type      | Constraints            | Notes                              |
|-------------|-----------|------------------------|------------------------------------|
| id          | UUID      | PK                     |                                    |
| event_id    | UUID      | FK → pothole_events.id |                                    |
| action      | TEXT      | NOT NULL               | `confirm`, `reject`, `mark_repaired`, `upvote` |
| reviewer_id | TEXT      | DEFAULT 'anonymous'    | placeholder for future auth        |
| comment     | TEXT      | nullable               | optional free-text                 |
| created_at  | TEXT      | NOT NULL DEFAULT NOW   |                                    |

## Indexes (SQLite)
```sql
CREATE INDEX idx_detections_media ON detections(media_id);
CREATE INDEX idx_events_status ON pothole_events(status);
CREATE INDEX idx_events_cluster ON pothole_events(cluster_id);
CREATE INDEX idx_reviews_event ON reviews(event_id);
```

## YOLO Dataset Format

See `data/processed/potholes_yolo/data.yaml`:
```yaml
path: data/processed/potholes_yolo
train: images/train
val: images/val
test: images/test
names:
  0: pothole
```

Labels are YOLO txt format: `<class_id> <x_center> <y_center> <width> <height>` (all normalised).

## GeoJSON Output Format (RFC 7946)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [lng, lat]
      },
      "properties": {
        "id": "uuid",
        "status": "confirmed",
        "severity": "medium",
        "detection_count": 3,
        "first_seen": "2026-06-01T00:00:00Z",
        "last_seen": "2026-06-15T00:00:00Z"
      }
    }
  ]
}
```
