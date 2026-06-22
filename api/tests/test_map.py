"""Tests for the map GeoJSON endpoint."""

import pytest
from httpx import ASGITransport, AsyncClient

from api.app.main import app


@pytest.mark.asyncio
async def test_geojson_returns_feature_collection():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/v1/map/geojson")
    assert resp.status_code == 200
    data = resp.json()
    assert data["type"] == "FeatureCollection"
    assert len(data["features"]) >= 1
    feat = data["features"][0]
    assert feat["type"] == "Feature"
    assert feat["geometry"]["type"] == "Point"
    assert "status" in feat["properties"]


@pytest.mark.asyncio
async def test_geojson_filter_by_status():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/v1/map/geojson?status=confirmed")
    assert resp.status_code == 200
    data = resp.json()
    for feat in data["features"]:
        assert feat["properties"]["status"] == "confirmed"
