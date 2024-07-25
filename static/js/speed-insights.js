import { SpeedInsights } from "@vercel/speed-insights/next";

// Example usage of SpeedInsights
function loadSpeedInsights() {
  SpeedInsights();
}

document.addEventListener('DOMContentLoaded', loadSpeedInsights);
