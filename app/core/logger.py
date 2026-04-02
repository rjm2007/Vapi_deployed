import logging
import os
import sys

fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")

logger = logging.getLogger("tebra_debug")
if not logger.handlers:
    logger.setLevel(logging.INFO)

    # stdout — visible in Render dashboard logs
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    # file — available locally
    os.makedirs("logs", exist_ok=True)
    fh = logging.FileHandler("logs/tebra_debug.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
