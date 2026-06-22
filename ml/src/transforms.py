"""Image transforms and augmentations for pothole detection."""

from typing import Any


def get_transforms(train: bool = True) -> Any:
    """Return Albumentations / YOLO transforms.

    Args:
        train: If True, include augmentations (flip, rotate, etc.).

    Returns:
        Transform pipeline (currently returns None — YOLO handles its own augs).
    """
    # YOLOv8 applies built-in augmentations via the `augment` flag during training.
    # Explicit Albumentations pipeline can be added here for custom transforms.
    return None
