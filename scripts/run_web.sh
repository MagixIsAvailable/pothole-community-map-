#!/usr/bin/env bash
# run_web.sh — start the React+Vite dev server
set -euo pipefail

cd "$(dirname "$0")/../web"
npm run dev
