"""
Keep-Alive Pinger for Render Free Tier
───────────────────────────────────────
Pings the /health endpoint every 10 minutes to prevent cold starts.

Usage:
    python keep_alive.py

Set RENDER_URL env var or edit the default below.
Run this on your local machine (or any always-on box) while calls are expected.
Press Ctrl+C to stop.
"""

import os
import time
import urllib.request

RENDER_URL = os.getenv("RENDER_URL", "https://vapi-deployed.onrender.com")
INTERVAL = 10 * 60  # 10 minutes

def ping():
    url = f"{RENDER_URL}/health"
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"[OK]  {resp.status} — {url}")
    except Exception as e:
        print(f"[ERR] {e} — {url}")

if __name__ == "__main__":
    print(f"Pinging {RENDER_URL}/health every {INTERVAL // 60} min. Ctrl+C to stop.\n")
    while True:
        ping()
        time.sleep(INTERVAL)
