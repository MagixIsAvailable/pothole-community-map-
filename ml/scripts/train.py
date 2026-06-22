#!/usr/bin/env python
"""YOLOv8 training script.

Usage:
    python ml/scripts/train.py --config ml/configs/train_yolov8n.yaml
"""

import argparse
from pathlib import Path

from ultralytics import YOLO


def main(config_path: str) -> None:
    """Train a YOLOv8 model from a config file."""
    # TODO: Parse YAML config for model, data, epochs, image size, etc.
    data_yaml = Path("data/processed/potholes_yolo/data.yaml")
    if not data_yaml.exists():
        raise FileNotFoundError(f"Dataset YAML not found: {data_yaml}")

    model = YOLO("yolov8n.pt")  # Start from pretrained nano weights
    results = model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=16,
        name="pothole_v1",
        exist_ok=True,
    )
    print(f"Training complete. Best model: {results.save_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train YOLOv8 pothole detector")
    parser.add_argument("--config", default="ml/configs/train_yolov8n.yaml")
    args = parser.parse_args()
    main(args.config)
