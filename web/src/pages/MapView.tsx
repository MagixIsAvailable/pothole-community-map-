/** MapView page — Leaflet map with pothole GeoJSON layer and filters. */

import { useEffect, useState } from "react";
import {
  MapContainer,
  TileLayer,
  GeoJSON,
  useMap,
} from "react-leaflet";
import type { GeoJSONResponse, PotholeFeature, PotholeStatus } from "../lib/types";
import { STATUS_COLORS } from "../lib/types";
import { fetchGeoJSON } from "../lib/api";
import FiltersPanel from "../components/map/FiltersPanel";

/** Recenter map when fitBounds is called externally via FiltersPanel */
function MapBoundsUpdater({ center }: { center: [number, number] | null }) {
  const map = useMap();
  useEffect(() => {
    if (center) {
      map.setView(center, 16);
    }
  }, [center, map]);
  return null;
}

function pointToLayer(feature: PotholeFeature, latlng: L.LatLng) {
  const status = feature.properties.status as PotholeStatus;
  const color = STATUS_COLORS[status] ?? "#999";
  return L.circleMarker(latlng, {
    radius: 10,
    fillColor: color,
    color: "#fff",
    weight: 2,
    fillOpacity: 0.85,
  });
}

function onEachFeature(feature: PotholeFeature, layer: L.Layer) {
  const p = feature.properties;
  layer.bindPopup(`
    <strong>Pothole</strong><br/>
    Status: <span style="color:${STATUS_COLORS[p.status]}">${p.status}</span><br/>
    Severity: ${p.severity}<br/>
    Detections: ${p.detection_count}<br/>
    First seen: ${p.first_seen}<br/>
    Last seen: ${p.last_seen}
  `);
}

function MapView() {
  const [data, setData] = useState<GeoJSONResponse | null>(null);
  const [statusFilter, setStatusFilter] = useState<string | null>(null);
  const [center, setCenter] = useState<[number, number] | null>(null);

  useEffect(() => {
    (async () => {
      const json = await fetchGeoJSON(statusFilter ?? undefined) as GeoJSONResponse;
      setData(json);
    })();
  }, [statusFilter]);

  const handleFitMarkers = () => {
    setCenter([51.5074, -0.1278]);
  };

  return (
    <div style={{ display: "flex", height: "calc(100vh - 56px)" }}>
      <FiltersPanel
        statusFilter={statusFilter}
        onStatusChange={setStatusFilter}
        onFitMarkers={handleFitMarkers}
      />
      <div style={{ flex: 1 }}>
        <MapContainer
          center={[51.5074, -0.1278]}
          zoom={14}
          style={{ width: "100%", height: "100%" }}
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <MapBoundsUpdater center={center} />
          {data && (
            <GeoJSON
              key={JSON.stringify(statusFilter)}
              data={data as never}
              pointToLayer={pointToLayer as never}
              onEachFeature={onEachFeature as never}
            />
          )}
        </MapContainer>
      </div>
    </div>
  );
}

export default MapView;
