/** About page. */

function About() {
  return (
    <div style={{ maxWidth: 640, margin: "0 auto", padding: "48px 24px" }}>
      <h2 style={{ marginBottom: 16 }}>About Pothole Community Map</h2>
      <p style={{ color: "var(--color-text-secondary)", lineHeight: 1.8 }}>
        This is an open-source community tool that uses machine learning to
        detect potholes from uploaded photos and videos, then displays them on
        an interactive map so residents and local authorities can track and fix
        them.
      </p>
      <h3 style={{ marginTop: 24, marginBottom: 8 }}>Tech Stack</h3>
      <ul style={{ color: "var(--color-text-secondary)", lineHeight: 2 }}>
        <li>ML: Ultralytics YOLOv8</li>
        <li>API: FastAPI (Python)</li>
        <li>Frontend: React + Vite + TypeScript + Leaflet</li>
        <li>Data: GeoJSON (RFC 7946)</li>
      </ul>
      <p style={{ marginTop: 24, color: "var(--color-text-secondary)" }}>
        Version 0.1.0 — MVP
      </p>
    </div>
  );
}

export default About;
