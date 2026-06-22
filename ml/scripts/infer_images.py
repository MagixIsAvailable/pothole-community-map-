#!/usr/bin/env python
"""Run YOLO inference on a directory of images.

Usage:
    python ml/scripts/infer_images.py --weights best.pt --source data/raw/uploads_sample/ --output ml/runs/predict/
"""

import argparse
from pathlib import Path

from ultralytics import YOLO


def main(weights: str, source: str, output: str, conf: float) -> None:
    """Run inference on a folder of images and save results."""
    model = YOLO(weights)
    results = model.predict(
        source=source,
        conf=conf,
        save=True,
        save_txt=True,
        project=output,
        name="image_inference",
        exist_ok=True,
    )
    print(f"Inference complete. {len(results)} images processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 image inference")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", default="ml/runs/predict")
    parser.add_argument("--conf", type=float, default=0.35)
    args = parser.parse_args()
    main(args.weights, args.source, args.output, args.conf)
