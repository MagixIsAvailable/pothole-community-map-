"""Tests for the events endpoint."""

import pytest
from httpx import ASGITransport, AsyncClient

from api.app.main import app


@pytest.mark.asyncio
async def test_list_events_returns_empty_list():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/v1/events")
    assert resp.status_code == 200
    assert resp.json() == []
