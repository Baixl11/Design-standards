#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="$HOME/Desktop/style-design-spec-skill"
rm -rf "$TARGET"
mkdir -p "$TARGET"
cp -R "$SCRIPT_DIR"/* "$TARGET"/
echo "已复制到：$TARGET"
