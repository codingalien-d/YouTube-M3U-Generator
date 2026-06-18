#!/usr/bin/python3

import os
import subprocess

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHANNEL_FILE = os.path.join(BASE_DIR, "..", "youtube_channel_info.txt")


def grab(url):
    try:
        stream_url = subprocess.check_output(
            ["yt-dlp", "-g", url],
            text=True
        ).strip()

        print(stream_url)

    except Exception:
        print("# Stream unavailable")


with open(CHANNEL_FILE) as f:
    for line in f:
        line = line.strip()

        if not line or line.startswith("~~"):
            continue

        if line.startswith("https://"):
            grab(line)
        else:
            parts = [x.strip() for x in line.split("|")]

            if len(parts) != 4:
                continue

            ch_name, grp_title, tvg_logo, tvg_id = parts

            print(
                f'\n#EXTINF:-1 group-title="{grp_title}" '
                f'tvg-logo="{tvg_logo}" '
                f'tvg-id="{tvg_id}",{ch_name}'
            )