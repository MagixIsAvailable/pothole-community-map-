/** Review page — list pothole events and change their status. */

import { useEffect, useState } from "react";
import { fetchEvents, submitReview } from "../lib/api";
import type { PotholeStatus } from "../lib/types";
import { STATUS_COLORS } from "../lib/types";

interface Event {
  id: string;
  lat: number;
  lng: number;
  status: PotholeStatus;
  severity: string;
  detection_ids: string[];
  first_seen_at: string | null;
}

function Review() {
  const [events, setEvents] = useState<Event[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const data = (await fetchEvents()) as Event[];
        setEvents(data);
      } catch {
        setEvents([]); // API not yet wired
      }
    })();
  }, []);

  const handleAction = async (eventId: string, action: string) => {
    try {
      await submitReview(eventId, action);
      setMessage(`Action "${action}" submitted for event ${eventId}`);
      // Refresh list
      const data = (await fetchEvents()) as Event[];
      setEvents(data);
    } catch {
      setMessage("Review endpoint not yet wired");
    }
  };

  return (
    <div style={{ maxWidth: 800, margin: "0 auto", padding: "32px 24px" }}>
      <h2 style={{ marginBottom: 24 }}>✅ Review Potholes</h2>
      {message && (
        <p style={{ padding: 12, background: "#dbeafe", borderRadius: 8, marginBottom: 16 }}>
          {message}
        </p>
      )}

      {events.length === 0 && (
        <p style={{ color: "var(--color-text-secondary)" }}>
          No events yet. Upload photos to detect potholes, then review them here.
        </p>
      )}

      {events.map((evt) => (
        <div
          key={evt.id}
          style={{
            background: "#fff",
            borderRadius: 8,
            padding: 16,
            marginBottom: 12,
            boxShadow: "var(--shadow)",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            flexWrap: "wrap",
            gap: 12,
          }}
        >
          <div>
            <strong>Event</strong>{" "}
            <span style={{ fontSize: "0.85rem", color: "var(--color-text-secondary)" }}>
              {evt.id.slice(0, 8)}...
            </span>
            <br />
            📍 {evt.lat.toFixed(4)}, {evt.lng.toFixed(4)}
            <br />
            <span
              style={{
                display: "inline-block",
                width: 10,
                height: 10,
                borderRadius: "50%",
                background: STATUS_COLORS[evt.status],
                marginRight: 6,
              }}
            />
            Status: {evt.status} | Severity: {evt.severity} | Detections: {evt.detection_ids.length}
          </div>
          <div style={{ display: "flex", gap: 8 }}>
            <button
              onClick={() => handleAction(evt.id, "confirm")}
              style={{ ...btnStyle, background: "#10b981" }}
            >
              Confirm
            </button>
            <button
              onClick={() => handleAction(evt.id, "reject")}
              style={{ ...btnStyle, background: "#ef4444" }}
            >
              Reject
            </button>
            <button
              onClick={() => handleAction(evt.id, "mark_repaired")}
              style={{ ...btnStyle, background: "#6366f1" }}
            >
              Repaired
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

const btnStyle: React.CSSProperties = {
  color: "#fff",
  border: "none",
  padding: "8px 14px",
  borderRadius: 6,
  fontSize: "0.85rem",
  cursor: "pointer",
  fontWeight: 600,
};

export default Review;
