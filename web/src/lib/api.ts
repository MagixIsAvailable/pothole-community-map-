/** API client for the Pothole Community Map backend. */

const BASE_URL = "/api/v1";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...options?.headers },
    ...options,
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`API error ${res.status}: ${body}`);
  }
  return res.json();
}

export async function healthCheck(): Promise<{ status: string }> {
  return request("/health");
}

export async function uploadMedia(
  file: File,
  lat?: number,
  lng?: number
): Promise<unknown> {
  const formData = new FormData();
  formData.append("file", file);
  if (lat != null) formData.append("lat", String(lat));
  if (lng != null) formData.append("lng", String(lng));
  const res = await fetch(`${BASE_URL}/uploads`, {
    method: "POST",
    body: formData,
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Upload error ${res.status}: ${body}`);
  }
  return res.json();
}

export async function fetchGeoJSON(
  status?: string,
  minConfidence?: number
): Promise<unknown> {
  const params = new URLSearchParams();
  if (status) params.set("status", status);
  if (minConfidence != null) params.set("min_confidence", String(minConfidence));
  const qs = params.toString();
  return request(`/map/geojson${qs ? `?${qs}` : ""}`);
}

export async function fetchEvents(): Promise<unknown> {
  return request("/events");
}

export async function submitReview(eventId: string, action: string): Promise<unknown> {
  return request("/reviews", {
    method: "POST",
    body: JSON.stringify({ event_id: eventId, action }),
  });
}
