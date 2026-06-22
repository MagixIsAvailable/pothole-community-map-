"""YOLOv8 inference runner for images and videos."""

from pathlib import Path
from typing import Any

from ultralytics import YOLO


def run_inference(
    weights: str,
    source: str | Path,
    conf: float = 0.35,
    iou: float = 0.45,
    save: bool = True,
    project: str = "ml/runs/predict",
    name: str = "inference",
    **kwargs: Any,
) -> Any:
    """Run YOLO inference on images or video.

    Args:
        weights: Path to trained .pt weights.
        source: Image file, directory, or video path.
        conf: Confidence threshold.
        iou: IoU threshold for NMS.
        save: Whether to save output images/video.
        project: Output directory root.
        name: Run name.
        **kwargs: Additional arguments passed to model.predict().

    Returns:
        List of ultralytics Results objects.
    """
    model = YOLO(weights)
    results = model.predict(
        source=str(source),
        conf=conf,
        iou=iou,
        save=save,
        project=project,
        name=name,
        exist_ok=True,
        **kwargs,
    )
    return results
