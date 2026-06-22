"""Dataset loading and YOLO data.yaml helpers."""

from pathlib import Path
from typing import Any


def load_dataset_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YOLO-format data.yaml and return it as a dict.

    Args:
        path: Path to data.yaml.

    Returns:
        Dict with keys: path, train, val, test, nc, names.
    """
    import yaml

    with open(path) as f:
        return yaml.safe_load(f)


def create_splits(
    image_dir: Path,
    label_dir: Path,
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    seed: int = 42,
) -> tuple[list[Path], list[Path], list[Path]]:
    """Split image files into train/val/test sets.

    Args:
        image_dir: Directory containing images.
        label_dir: Directory containing YOLO-format labels (must match image names).
        train_ratio: Fraction for training.
        val_ratio: Fraction for validation. Remainder goes to test.
        seed: Random seed for reproducibility.

    Returns:
        Tuple of (train_files, val_files, test_files).
    """
    import random

    random.seed(seed)
    image_files = sorted(image_dir.glob("*"))
    if not image_files:
        # Try common image extensions
        image_files = sorted(
            f for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.tiff")
            for f in image_dir.glob(ext)
        )

    # Ensure label exists for each image
    image_files = [
        f for f in image_files
        if (label_dir / f"{f.stem}.txt").exists()
    ]

    random.shuffle(image_files)
    n = len(image_files)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train_files = image_files[:n_train]
    val_files = image_files[n_train : n_train + n_val]
    test_files = image_files[n_train + n_val :]

    return train_files, val_files, test_files
