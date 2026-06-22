# Evaluation Plan — Pothole Detection Model

## Objectives
1. Measure detection accuracy on held-out test set.
2. Benchmark inference speed on CPU.
3. Validate clustering quality on real GPS-tagged samples.

## Metrics

### Detection
| Metric       | Target (v1) | Description                        |
|-------------|-------------|------------------------------------|
| mAP@50      | ≥ 0.50      | Mean Average Precision at IoU 0.5  |
| mAP@50-95   | ≥ 0.30      | mAP averaged over IoU 0.5–0.95     |
| Precision   | ≥ 0.60      | TP / (TP + FP)                     |
| Recall      | ≥ 0.50      | TP / (TP + FN)                     |

### Speed
| Metric              | Target (v1) | Description                    |
|--------------------|-------------|--------------------------------|
| Inference latency   | < 3 s       | Per 640×640 image on CPU       |
| Video throughput    | > 2 fps     | Frames per second on CPU       |

### Clustering
| Metric              | Target (v1) | Description                        |
|--------------------|-------------|------------------------------------|
| Cluster purity      | > 0.80      | Same pothole → same cluster        |
| Redundancy rate     | < 20%       | Duplicate events for same pothole  |

## Test Protocol
1. Run `ml/scripts/evaluate.py` on the test split.
2. Profile inference with `ml/scripts/infer_images.py` on 100 sample images.
3. Manually inspect 50 random detections for qualitative review.
4. Test clustering on a small GPS-tagged sample set (20–50 images).

## Pass/Fail Criteria
- All detection metrics above targets → **pass**.
- One metric below target → investigate, retrain with more data.
- Multiple metrics below → revisit architecture or dataset quality.
