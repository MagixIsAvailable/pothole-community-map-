"""Upload endpoint — accept media and return mock detections."""

import uuid
from pathlib import Path
from typing import Any

from fastapi import APIRouter, File, Form, UploadFile

from api.app.core.config import get_settings
from api.app.schemas.uploads import UploadResponse

router = APIRouter()
settings = get_settings()


def _save_upload(file: UploadFile) -> Path:
    """Save uploaded file to storage/uploads/ with a unique name."""
    ext = Path(file.filename).suffix if file.filename else ".bin"
    dest = settings.storage_root / "uploads" / f"{uuid.uuid4().hex}{ext}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        f.write(file.file.read())
    return dest


def _mock_detections(media_id: str) -> list[dict[str, Any]]:
    """Generate mock YOLO-style detection results for MVP testing."""
    return [
        {
            "id": str(uuid.uuid4()),
            "media_id": media_id,
            "class_id": 0,
            "class_name": "pothole",
            "confidence": 0.87,
            "x_center": 0.45,
            "y_center": 0.60,
            "width": 0.12,
            "height": 0.08,
        },
        {
            "id": str(uuid.uuid4()),
            "media_id": media_id,
            "class_id": 0,
            "class_name": "pothole",
            "confidence": 0.72,
            "x_center": 0.78,
            "y_center": 0.35,
            "width": 0.09,
            "height": 0.11,
        },
    ]


@router.post("", response_model=UploadResponse)
async def upload_media(
    file: UploadFile = File(...),
    lat: float | None = Form(None),
    lng: float | None = Form(None),
) -> dict[str, Any]:
    """Accept an image/video, save it, and return mock detections."""
    saved_path = _save_upload(file)
    media_id = str(uuid.uuid4())

    detections = _mock_detections(media_id)

    return {
        "media_id": media_id,
        "filename": file.filename,
        "filepath": str(saved_path),
        "media_type": "image" if (file.content_type or "").startswith("image") else "video",
        "lat": lat or settings.DEFAULT_LAT,
        "lng": lng or settings.DEFAULT_LNG,
        "detections": detections,
    }
