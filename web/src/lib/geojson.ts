/** GeoJSON helper utilities. */

import type { GeoJSONResponse, PotholeFeature } from "./types";

export function filterByStatus(
  data: GeoJSONResponse,
  status: string | null
): GeoJSONResponse {
  if (!status) return data;
  return {
    ...data,
    features: data.features.filter(
      (f: PotholeFeature) => f.properties.status === status
    ),
  };
}

export function countByStatus(data: GeoJSONResponse): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const f of data.features) {
    const s = f.properties.status;
    counts[s] = (counts[s] || 0) + 1;
  }
  return counts;
}
