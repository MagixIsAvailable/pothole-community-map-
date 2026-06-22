# Web Frontend — Pothole Community Map

React 18 + Vite + TypeScript + Leaflet frontend.

## Quick Start

```bash
cd web
npm install
npm run dev
```

Open http://localhost:5173

## Pages

| Route    | Page      | Description                         |
|----------|-----------|-------------------------------------|
| `/`      | Home      | Landing page with navigation        |
| `/map`   | MapView   | Leaflet map with pothole GeoJSON    |
| `/upload`| Upload    | Upload photo/video + view detections|
| `/review`| Review    | Review and change pothole statuses  |
| `/about` | About     | Project information                 |

## Architecture

- `src/lib/types.ts` — shared TypeScript types
- `src/lib/api.ts` — API client functions
- `src/lib/geojson.ts` — GeoJSON helpers
- `src/pages/` — page-level components (one per route)
- `src/components/` — reusable UI components

## Proxy

The Vite dev server proxies `/api` requests to the FastAPI backend on `http://127.0.0.1:8000`.
