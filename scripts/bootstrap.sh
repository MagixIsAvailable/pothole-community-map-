#!/usr/bin/env bash
# bootstrap.sh — one-time setup for the pothole community map monorepo
set -euo pipefail

echo "=== Pothole Community Map — Bootstrap ==="

# Python virtualenv
if [ ! -d ".venv" ]; then
    echo "Creating Python virtualenv..."
    python3 -m venv .venv
fi
source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -e ".[dev]"

# Web dependencies
echo "Installing web dependencies..."
cd web && npm install && cd ..

# Copy .env if not present
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo ".env created from .env.example — review settings before running."
fi

echo "=== Bootstrap complete ==="
