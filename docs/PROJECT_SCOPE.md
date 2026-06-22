# Project Scope — Pothole Community Map

## Mission
Enable communities to crowdsource pothole detection and track repair progress
using computer vision and an interactive map.

## Problem
- Potholes cause vehicle damage and safety hazards.
- Municipalities lack real-time awareness of road conditions.
- Citizens have no easy way to report and track potholes.

## Solution
A web-based platform where anyone can:
1. Upload a photo/video of a road surface.
2. Get automatic pothole detection via YOLOv8.
3. See results on a live map.
4. Help review and track repair status.

## Users (v1)
- **Community members**: Upload photos, view the map.
- **Reviewers**: Confirm/reject/repair pothole events.
- **Municipalities** (future): API access, bulk export.

## Success Metrics
- Detection accuracy (mAP) above 0.50.
- Upload-to-detection latency under 3 seconds (local CPU).
- Map loads in under 2 seconds.
- Review workflow supports full status lifecycle.
