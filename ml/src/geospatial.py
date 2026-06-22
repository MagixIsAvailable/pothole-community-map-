"""GPS extraction from EXIF and geotagging utilities."""

from pathlib import Path
from typing import Any


def extract_gps(image_path: str | Path) -> tuple[float, float] | None:
    """Extract GPS latitude and longitude from image EXIF data.

    Args:
        image_path: Path to an image file.

    Returns:
        Tuple of (latitude, longitude) or None if no GPS data.
    """
    try:
        from PIL import Image
        from PIL.ExifTags import GPSTAGS
    except ImportError:
        return None

    try:
        img = Image.open(image_path)
        exif = img._getexif()
        if not exif:
            return None

        gps_info: dict[int, Any] = {}
        for tag_id, value in exif.items():
            tag_name = GPSTAGS.get(tag_id, tag_id)
            gps_info[tag_name] = value

        if "GPSLatitude" not in gps_info or "GPSLongitude" not in gps_info:
            return None

        def _to_decimal(dms: tuple, ref: str) -> float:
            """Convert DMS tuple to decimal degrees."""
            d, m, s = dms
            decimal = float(d) + float(m) / 60.0 + float(s) / 3600.0
            if ref in ("S", "W"):
                decimal = -decimal
            return decimal

        lat = _to_decimal(gps_info["GPSLatitude"], gps_info.get("GPSLatitudeRef", "N"))
        lng = _to_decimal(gps_info["GPSLongitude"], gps_info.get("GPSLongitudeRef", "E"))
        return lat, lng
    except Exception:
        return None


def geotag_detections(
    media_dir: Path,
    detections: list[dict[str, Any]],
    default_lat: float = 51.5074,
    default_lng: float = -0.1278,
) -> list[dict[str, Any]]:
    """Attach GPS coordinates to detection records.

    Args:
        media_dir: Directory containing uploaded media.
        detections: List of detection dicts with 'filepath' key.
        default_lat: Fallback latitude.
        default_lng: Fallback longitude.

    Returns:
        Detections list with 'lat' and 'lng' appended.
    """
    for det in detections:
        filepath = det.get("filepath", "")
        gps = extract_gps(filepath) if filepath else None
        det["lat"] = gps[0] if gps else default_lat
        det["lng"] = gps[1] if gps else default_lng
    return detections
