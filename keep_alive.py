"""
Keep-Alive Pinger for Render Free Tier
───────────────────────────────────────
Pings the /health endpoint every 8 minutes to prevent cold starts.
Render spins down after 15 minutes of inactivity — 8 min gives a safe buffer.

Usage:
    python keep_alive.py

Set RENDER_URL env var or edit the default below.
Run this on your local machine (or any always-on box) while calls are expected.
Press Ctrl+C to stop.
"""

import os
import time
import urllib.request
from datetime import datetime

RENDER_URL = os.getenv("RENDER_URL", "https://vapi-deployed-1.onrender.com")
INTERVAL = 8 * 60  # 8 minutes — safe buffer before Render's 15-min spin-down

def ping():
    url = f"{RENDER_URL}/health"
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"[{ts}] [OK]  {resp.status} — {url}")
    except Exception as e:
        print(f"[{ts}] [ERR] {e} — {url}")

if __name__ == "__main__":
    print(f"Pinging {RENDER_URL}/health every {INTERVAL // 60} min. Ctrl+C to stop.\n")
    while True:
        ping()
        time.sleep(INTERVAL)
