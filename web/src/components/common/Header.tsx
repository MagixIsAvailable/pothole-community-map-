/** App header with responsive nav links. */

import { Link, useLocation } from "react-router-dom";

const NAV = [
  { to: "/", label: "Home" },
  { to: "/map", label: "Map" },
  { to: "/upload", label: "Upload" },
  { to: "/review", label: "Review" },
  { to: "/about", label: "About" },
];

function Header() {
  const location = useLocation();

  return (
    <header
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        height: "56px",
        background: "#fff",
        borderBottom: "1px solid var(--color-border)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 24px",
        zIndex: 999,
        boxShadow: "var(--shadow)",
      }}
    >
      <Link
        to="/"
        style={{ fontWeight: 700, fontSize: "1.1rem", color: "var(--color-text)" }}
      >
        🛣️ Pothole Map
      </Link>
      <nav style={{ display: "flex", gap: "20px" }}>
        {NAV.map(({ to, label }) => (
          <Link
            key={to}
            to={to}
            style={{
              fontSize: "0.9rem",
              fontWeight: location.pathname === to ? 600 : 400,
              color:
                location.pathname === to
                  ? "var(--color-primary)"
                  : "var(--color-text-secondary)",
              padding: "4px 0",
              borderBottom:
                location.pathname === to
                  ? "2px solid var(--color-primary)"
                  : "2px solid transparent",
              transition: "all 0.15s",
            }}
          >
            {label}
          </Link>
        ))}
      </nav>
    </header>
  );
}

export default Header;
