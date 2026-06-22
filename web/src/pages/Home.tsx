/** Home page. */

import { Link } from "react-router-dom";

function Home() {
  return (
    <div style={{ maxWidth: 720, margin: "0 auto", padding: "48px 24px" }}>
      <h1 style={{ fontSize: "2rem", marginBottom: 16 }}>
        🛣️ Pothole Community Map
      </h1>
      <p style={{ color: "var(--color-text-secondary)", marginBottom: 32, fontSize: "1.1rem" }}>
        Help your community track and fix potholes. Upload a photo, see
        detections on the map, and review reported potholes.
      </p>
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
        <Link to="/map">
          <button style={btnStyle}>🗺️ View Map</button>
        </Link>
        <Link to="/upload">
          <button style={{ ...btnStyle, background: "#10b981" }}>
            📤 Upload Photo
          </button>
        </Link>
        <Link to="/review">
          <button style={{ ...btnStyle, background: "#f59e0b" }}>
            ✅ Review Potholes
          </button>
        </Link>
      </div>
    </div>
  );
}

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

export default Home;
