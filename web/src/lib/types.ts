/** Shared TypeScript types for the frontend. */

export interface DetectionResult {
  id: string;
  media_id: string;
  class_id: number;
  class_name: string;
  confidence: number;
  x_center: number;
  y_center: number;
  width: number;
  height: number;
}

export interface UploadResponse {
  media_id: string;
  filename: string;
  filepath: string;
  media_type: string;
  lat: number | null;
  lng: number | null;
  detections: DetectionResult[];
}

export interface PotholeFeature {
  type: "Feature";
  geometry: {
    type: "Point";
    coordinates: [number, number];
  };
  properties: PotholeProperties;
}

export interface PotholeProperties {
  id: string;
  status: PotholeStatus;
  severity: PotholeSeverity;
  detection_count: number;
  first_seen: string;
  last_seen: string;
}

export interface GeoJSONResponse {
  type: "FeatureCollection";
  features: PotholeFeature[];
}

export type PotholeStatus =
  | "detected"
  | "under_review"
  | "confirmed"
  | "rejected"
  | "repaired";

export type PotholeSeverity = "low" | "medium" | "high" | "unknown";

export const STATUS_COLORS: Record<PotholeStatus, string> = {
  detected: "#f59e0b",
  under_review: "#3b82f6",
  confirmed: "#ef4444",
  rejected: "#6b7280",
  repaired: "#10b981",
};

export const SEVERITY_COLORS: Record<PotholeSeverity, string> = {
  low: "#eab308",
  medium: "#f97316",
  high: "#ef4444",
  unknown: "#9ca3af",
};
