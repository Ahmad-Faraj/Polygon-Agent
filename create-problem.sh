#!/usr/bin/env bash
# Polygon Agent problem creator
# The agent uses AGENTS.md and this repo end-to-end.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"
python polygon_agent.py list 2>/dev/null || true
echo ""
echo "Polygon Agent -- ECPC 2026 Problem Creator"
echo "Describe your problem (Ctrl+D when done):"
cat
