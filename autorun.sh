#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

python3 -m pip install -q requests yt-dlp

cd "$SCRIPT_DIR/scripts"

python3 youtube_m3ugrabber.py > ../youtube.m3u

cd ..

touch Original.m3u

cat youtube.m3u Original.m3u > out.m3u

echo "m3u grabbed"