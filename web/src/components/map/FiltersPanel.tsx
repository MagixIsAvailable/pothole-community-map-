/** Filters sidebar panel for the map page. */

import type { PotholeStatus } from "../../lib/types";

interface Props {
  statusFilter: string | null;
  onStatusChange: (status: string | null) => void;
  onFitMarkers: () => void;
}

const STATUSES: PotholeStatus[] = [
  "detected",
  "under_review",
  "confirmed",
  "rejected",
  "repaired",
];

function FiltersPanel({ statusFilter, onStatusChange, onFitMarkers }: Props) {
  return (
    <aside
      style={{
        width: 240,
        background: "#fff",
        borderRight: "1px solid var(--color-border)",
        padding: 20,
        overflowY: "auto",
        flexShrink: 0,
      }}
    >
      <h3 style={{ marginBottom: 16 }}>Filters</h3>

      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", fontWeight: 600, marginBottom: 6 }}>Status</label>
        <select
          value={statusFilter ?? ""}
          onChange={(e) => onStatusChange(e.target.value || null)}
          style={{
            width: "100%",
            padding: "8px 10px",
            borderRadius: 6,
            border: "1px solid var(--color-border)",
            fontSize: "0.9rem",
          }}
        >
          <option value="">All</option>
          {STATUSES.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
      </div>

      <button
        onClick={onFitMarkers}
        style={{
          width: "100%",
          padding: "10px 0",
          background: "#3b82f6",
          color: "#fff",
          border: "none",
          borderRadius: 6,
          cursor: "pointer",
          fontWeight: 600,
          marginTop: 12,
        }}
      >
        🎯 Fit Markers
      </button>
    </aside>
  );
}

export default FiltersPanel;
