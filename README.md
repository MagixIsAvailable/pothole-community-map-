# 🛣️ Pothole Community Map

Community-driven pothole detection and live mapping system using YOLOv8 and Leaflet.

## Overview

Upload a photo or video of a road surface → automatically detect potholes →
see them on an interactive map → review and track repair status.

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  web/    │────▶│  api/    │────▶│  ml/     │
│ React    │     │ FastAPI  │     │ YOLOv8   │
│ Leaflet  │     │ SQLite   │     │ scripts  │
└──────────┘     └──────────┘     └──────────┘
```

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Git

### One-time setup
```bash
# Clone and enter the repo
git clone <your-repo-url>
cd pothole-community-map

# Run the bootstrap script
bash scripts/bootstrap.sh
```

### Start the app (two terminals)

**Windows (PowerShell):**
```powershell
# Terminal 1 — API backend
pip install fastapi uvicorn sqlalchemy pydantic pydantic-settings python-multipart aiofiles httpx
$env:PYTHONPATH="."
uvicorn api.app.main:app --reload --host 127.0.0.1 --port 8000
# → http://127.0.0.1:8000/docs

# Terminal 2 — Web frontend
cd web
npm install
npm run dev
# → http://localhost:5173
```

**macOS / Linux:**
```bash
# Terminal 1 — API backend
bash scripts/run_api.sh
# → http://127.0.0.1:8000/docs

# Terminal 2 — Web frontend
bash scripts/run_web.sh
# → http://localhost:5173
```

## Project Structure

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for full details.

| Directory    | Purpose                                      |
|-------------|----------------------------------------------|
| `api/`      | FastAPI backend (REST, SQLite, services)     |
| `web/`      | React + Vite + TypeScript frontend           |
| `ml/`       | ML pipeline (YOLOv8 training, inference)     |
| `docs/`     | Project documentation                        |
| `data/`     | Datasets (raw, interim, processed, exports)  |
| `storage/`  | Uploaded media and derived files             |
| `scripts/`  | Shell scripts for common tasks               |

## Key Features (v1 MVP)
- 📤 Upload images/videos and get YOLO detections.
- 🗺️ Interactive Leaflet map with GeoJSON pothole markers.
- ✅ Review workflow: detected → confirmed → repaired.
- 📊 Filter by status, severity, date.
- 📁 Export data as GeoJSON / CSV.

## Running Tests
```bash
# API tests
pytest api/tests/ -v

# Web type-check
cd web && npx tsc --noEmit
```

## Configuration
Copy `.env.example` to `.env` and adjust settings. All config keys are documented in `api/app/core/config.py`.

## Status Values
| Status        | Description                        |
|--------------|------------------------------------|
| `detected`    | Auto-detected, not yet reviewed    |
| `under_review`| Being reviewed                     |
| `confirmed`   | Verified as a real pothole         |
| `rejected`    | False positive                     |
| `repaired`    | Pothole has been filled            |

## Contributing
See [MVP.md](docs/MVP.md) for scope and [DECISIONS.md](docs/DECISIONS.md) for architectural decisions.

## License
MIT — see [LICENSE](LICENSE).

## Repo structure
- `ml/` model training, inference, geotagging, exports
- `api/` FastAPI backend and worker logic
- `web/` map UI and upload/review frontend
- `docs/` project scope, architecture, data schema, API spec
- `data/` raw, interim, processed datasets
