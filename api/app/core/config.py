"""Application configuration via environment variables."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central settings loaded from .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    APP_NAME: str = "pothole-community-map"
    DEBUG: bool = True
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    # Database
    DATABASE_URL: str = "sqlite:///./pothole_map.db"

    # Upload
    MAX_UPLOAD_SIZE_MB: int = 50

    # ML
    YOLO_MODEL: str = "yolov8n.pt"
    YOLO_CONFIDENCE_THRESHOLD: float = 0.35
    YOLO_IMAGE_SIZE: int = 640

    # Geo-tagging
    DEFAULT_LAT: float = 51.5074
    DEFAULT_LNG: float = -0.1278
    CLUSTER_EPS_METERS: float = 15.0
    CLUSTER_MIN_SAMPLES: int = 2

    # CORS
    CORS_ORIGINS: str = "http://localhost:5173"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

    @property
    def storage_root(self) -> Path:
        return Path(__file__).resolve().parents[3] / "storage"


@lru_cache
def get_settings() -> Settings:
    return Settings()
