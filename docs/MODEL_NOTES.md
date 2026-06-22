# Model Notes — Pothole Detection

## Model Choice
- **Architecture**: YOLOv8 Nano (`yolov8n.pt`) for v1 baseline.
- **Rationale**: Fast CPU inference (< 3 s per image), good accuracy on small objects like potholes.
- **Future**: Upgrade to YOLOv8 Small/Medium if more accuracy needed.

## Dataset Strategy
Four public pothole datasets merged into a single YOLO-format dataset:
1. **Kaggle** — annotated-potholes-dataset
2. **Roboflow** — pothole-detection-v2
3. **HRP4K** — high-resolution pothole 4K
4. **Pothole Mix** — miscellaneous pothole images

## Preprocessing
- Resize all images to 640×640 (YOLOv8 default).
- Convert all annotations to YOLO txt format (normalised cx, cy, w, h).
- 70/15/15 train/val/test split with fixed seed (42).

## Training Config
- Start from COCO-pretrained `yolov8n.pt`.
- 50 epochs for nano, 100 for small.
- Batch size 16 (nano) / 8 (small) for CPU training.
- SGD with momentum 0.937, weight decay 5e-4.
- Default YOLOv8 augmentations: mosaic, mixup, hsv, flip.

## Evaluation
- Primary metric: mAP@50 (mean Average Precision at IoU=0.5).
- Secondary: mAP@50-95, precision, recall.
- Per-class metrics since we only have one class (pothole).

## Known Limitations
- Single-class detector; won't distinguish crack, patch, manhole.
- Trained on daytime, clear-weather images; may underperform in rain/night.
- CPU-bound inference; GPU recommended for video processing at scale.
