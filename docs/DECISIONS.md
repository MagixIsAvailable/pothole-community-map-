# Architecture Decisions — Pothole Community Map

## ADR-001: SQLite for MVP
**Decision**: Use SQLite with SQLAlchemy ORM for local dev.
**Rationale**: Zero setup, single file, easy to reason about.
**Trade-off**: No concurrent writes; migrate to Postgres/PostGIS for production.
**Migration path**: SQLAlchemy abstracts the dialect; swap `DATABASE_URL` and add PostGIS geo columns.

## ADR-002: GeoJSON as Wire Format
**Decision**: Serve map data as GeoJSON FeatureCollection over REST.
**Rationale**: Native Leaflet support, no server-side rendering needed.
**Trade-off**: No spatial queries at DB level; filtering done in API layer.
**Migration path**: Add PostGIS when spatial queries are needed (e.g., "find potholes within 500 m").

## ADR-003: Single pothole Class (v1)
**Decision**: Detect only `pothole` class in v1.
**Rationale**: Simpler dataset merge, faster training, clearer MVP scope.
**Future**: Add `crack`, `patch`, `manhole` classes when multi-class datasets are curated.

## ADR-004: In-Process Task Queue
**Decision**: Run detection synchronously in the request thread for MVP.
**Rationale**: Simpler architecture; acceptable latency for single-image uploads.
**Future**: Replace with ARQ (Redis-backed) when async processing is needed.

## ADR-005: CPU-First Training
**Decision**: Default to CPU training in configs.
**Rationale**: Maximises accessibility; any developer can run the pipeline.
**GPU support**: Change `device: cuda` in config YAML files.

## ADR-006: No Auth in v1
**Decision**: All endpoints are open; reviewer_id defaults to "anonymous".
**Rationale**: Focus on core detection and mapping; auth adds complexity.
**Future**: Add JWT-based auth with FastAPI dependency injection.
