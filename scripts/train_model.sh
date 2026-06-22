#!/usr/bin/env bash
# train_model.sh — train the YOLOv8 pothole detector
set -euo pipefail

source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
cd "$(dirname "$0")/.."
python ml/scripts/train.py --config ml/configs/train_yolov8n.yaml
