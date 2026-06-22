"""Tests for the upload endpoint."""

import pytest
from httpx import ASGITransport, AsyncClient

from api.app.main import app


@pytest.mark.asyncio
async def test_upload_image_returns_detections():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        files = {"file": ("test.jpg", b"fake-image-bytes", "image/jpeg")}
        data = {"lat": "51.5074", "lng": "-0.1278"}
        resp = await client.post("/api/v1/uploads", files=files, data=data)
    assert resp.status_code == 200
    body = resp.json()
    assert "media_id" in body
    assert body["detections"] is not None
    assert len(body["detections"]) > 0
    assert body["detections"][0]["class_name"] == "pothole"


@pytest.mark.asyncio
async def test_upload_without_latlng_uses_defaults():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        files = {"file": ("test.png", b"fake-png-bytes", "image/png")}
        resp = await client.post("/api/v1/uploads", files=files)
    assert resp.status_code == 200
    body = resp.json()
    assert body["lat"] == 51.5074
    assert body["lng"] == -0.1278
