"""YOLOv8 training wrapper."""

from pathlib import Path
from typing import Any

from ultralytics import YOLO


def train_model(
    model_name: str = "yolov8n.pt",
    data_yaml: str | Path = "data/processed/potholes_yolo/data.yaml",
    epochs: int = 50,
    imgsz: int = 640,
    batch: int = 16,
    project: str = "ml/runs/train",
    name: str = "pothole_v1",
    **kwargs: Any,
) -> Any:
    """Train a YOLOv8 model for pothole detection.

    Args:
        model_name: Pretrained YOLO model checkpoint or YAML.
        data_yaml: Path to dataset configuration.
        epochs: Number of training epochs.
        imgsz: Input image size.
        batch: Batch size.
        project: Directory to save training outputs.
        name: Run name.
        **kwargs: Additional arguments passed to model.train().

    Returns:
        Training results object.
    """
    model = YOLO(model_name)
    results = model.train(
        data=str(data_yaml),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        project=project,
        name=name,
        exist_ok=True,
        **kwargs,
    )
    return results
