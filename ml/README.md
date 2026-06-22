# ML Pipeline — Pothole Community Map

## Overview

The `ml/` directory contains the machine learning pipeline for pothole detection:

- **src/** — Reusable Python library (datasets, transforms, training, inference, geospatial, clustering).
- **scripts/** — Runnable CLI entry points for each step.
- **notebooks/** — Jupyter notebooks for exploration and documented workflows.
- **configs/** — YAML configuration files for training and inference runs.
- **models/** — Saved weights and checkpoints (gitignored).
- **runs/** — Training, validation, and prediction outputs (gitignored).

## Quick Start

```bash
# 1. Download and prepare datasets
python ml/scripts/download_datasets.py
python ml/scripts/convert_to_yolo.py
python ml/scripts/merge_datasets.py

# 2. Train the model
python ml/scripts/train.py --config ml/configs/train_yolov8n.yaml

# 3. Evaluate
python ml/scripts/evaluate.py --weights ml/runs/train/pothole_v1/weights/best.pt

# 4. Run inference on sample images
python ml/scripts/infer_images.py --weights ml/runs/train/pothole_v1/weights/best.pt --source data/raw/uploads_sample/

# 5. Geotag + cluster + export
python ml/scripts/geotag.py --media-dir storage/uploads/
python ml/scripts/deduplicate_events.py --detections data/exports/csv/detections.csv
python ml/scripts/export_geojson.py --events data/exports/csv/events.csv
```

## Library Usage

```python
from ml.src import train_model, evaluate_model, run_inference, set_seed

set_seed(42)
results = train_model(model_name="yolov8n.pt", epochs=50)
metrics = evaluate_model("ml/runs/train/pothole_v1/weights/best.pt")
detections = run_inference("best.pt", "data/raw/uploads_sample/")
```
