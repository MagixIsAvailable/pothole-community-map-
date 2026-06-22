#!/usr/bin/env python
"""YOLOv8 model evaluation script.

Usage:
    python ml/scripts/evaluate.py --weights ml/runs/train/pothole_v1/weights/best.pt
"""

import argparse

from ultralytics import YOLO


def main(weights: str) -> None:
    """Evaluate a trained YOLO model on the test set."""
    model = YOLO(weights)
    metrics = model.val(data="data/processed/potholes_yolo/data.yaml")
    print(f"mAP@50: {metrics.box.map50:.4f}")
    print(f"mAP@50-95: {metrics.box.map:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate YOLOv8 pothole detector")
    parser.add_argument("--weights", required=True, help="Path to trained model weights")
    args = parser.parse_args()
    main(args.weights)
