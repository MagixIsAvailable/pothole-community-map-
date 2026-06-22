"""YOLOv8 model evaluation."""

from typing import Any

from ultralytics import YOLO


def evaluate_model(
    weights: str,
    data_yaml: str = "data/processed/potholes_yolo/data.yaml",
    **kwargs: Any,
) -> dict[str, float]:
    """Evaluate a trained YOLO model and return key metrics.

    Args:
        weights: Path to .pt weights file.
        data_yaml: Path to dataset YAML.
        **kwargs: Additional arguments passed to model.val().

    Returns:
        Dict with mAP50, mAP50-95, precision, recall.
    """
    model = YOLO(weights)
    metrics = model.val(data=data_yaml, **kwargs)
    return {
        "mAP50": float(metrics.box.map50),
        "mAP50-95": float(metrics.box.map),
        "precision": float(metrics.box.mp),
        "recall": float(metrics.box.mr),
    }
