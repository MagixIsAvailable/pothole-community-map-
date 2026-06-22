#!/usr/bin/env bash
# run_api.sh — start the FastAPI backend
set -euo pipefail

source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
cd "$(dirname "$0")/.."
uvicorn api.app.main:app --reload --host 127.0.0.1 --port 8000
