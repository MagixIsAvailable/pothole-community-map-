#!/usr/bin/env python
"""Run YOLO inference on a video file, extracting per-frame detections.

Usage:
    python ml/scripts/infer_video.py --weights best.pt --source video.mp4 --output ml/runs/predict/
"""

import argparse

from ultralytics import YOLO


def main(weights: str, source: str, output: str, conf: float) -> None:
    """Run inference on a video, saving annotated output and per-frame detections."""
    model = YOLO(weights)
    results = model.predict(
        source=source,
        conf=conf,
        save=True,
        project=output,
        name="video_inference",
        exist_ok=True,
    )
    print(f"Video inference complete. Frames processed: {len(results)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 video inference")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", default="ml/runs/predict")
    parser.add_argument("--conf", type=float, default=0.35)
    args = parser.parse_args()
    main(args.weights, args.source, args.output, args.conf)
