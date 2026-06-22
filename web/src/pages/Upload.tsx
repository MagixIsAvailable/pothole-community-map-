/** Upload page — image/video upload form with mock detection results. */

import { useState, type FormEvent } from "react";
import type { UploadResponse } from "../lib/types";
import { uploadMedia } from "../lib/api";

function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [lat, setLat] = useState<string>("");
  const [lng, setLng] = useState<string>("");
  const [result, setResult] = useState<UploadResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    setError(null);
    try {
      const data = (await uploadMedia(
        file,
        lat ? parseFloat(lat) : undefined,
        lng ? parseFloat(lng) : undefined
      )) as UploadResponse;
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", padding: "32px 24px" }}>
      <h2 style={{ marginBottom: 24 }}>📤 Upload Road Photo</h2>

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 16 }}>
        <input
          type="file"
          accept="image/*,video/*"
          onChange={(e) => setFile(e.target.files?.[0] ?? null)}
          required
        />
        <div style={{ display: "flex", gap: 12 }}>
          <input
            type="number"
            placeholder="Latitude (optional)"
            value={lat}
            onChange={(e) => setLat(e.target.value)}
            step="any"
            style={inputStyle}
          />
          <input
            type="number"
            placeholder="Longitude (optional)"
            value={lng}
            onChange={(e) => setLng(e.target.value)}
            step="any"
            style={inputStyle}
          />
        </div>
        <button type="submit" disabled={!file || loading} style={btnStyle}>
          {loading ? "Uploading..." : "Upload & Detect"}
        </button>
      </form>

      {error && <p style={{ color: "#ef4444", marginTop: 16 }}>{error}</p>}

      {result && (
        <div style={{ marginTop: 24, padding: 16, background: "#fff", borderRadius: 8, boxShadow: "var(--shadow)" }}>
          <h3>Detection Results</h3>
          <p>Media ID: {result.media_id}</p>
          <p>Location: {result.lat?.toFixed(4)}, {result.lng?.toFixed(4)}</p>
          <p>Found {result.detections.length} detection(s):</p>
          <ul>
            {result.detections.map((d) => (
              <li key={d.id}>
                {d.class_name} — confidence: {(d.confidence * 100).toFixed(1)}%
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

const inputStyle: React.CSSProperties = {
  flex: 1,
  padding: "10px 12px",
  border: "1px solid var(--color-border)",
  borderRadius: 8,
  fontSize: "0.95rem",
};

const btnStyle: React.CSSProperties = {
  background: "#3b82f6",
  color: "#fff",
  border: "none",
  padding: "12px 24px",
  borderRadius: 8,
  fontSize: "1rem",
  cursor: "pointer",
  fontWeight: 600,
};

export default Upload;
