# ─────────────────────────────────────────────────────────────────────────────
# Rausch PT — FastAPI App Entry Point
#
# RUN:
#   uvicorn app.main:app --reload --port 8000
#
# (Run this command from the fastapi/ project root directory)
# ─────────────────────────────────────────────────────────────────────────────

import hmac
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import VAPI_SERVER_SECRET
from app.api import availability, appointments, leads, debug

app = FastAPI(title="Rausch PT Tebra API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.middleware("http")
async def verify_vapi_secret(request: Request, call_next):
    """Reject POST requests that don't carry the correct x-vapi-secret header."""
    if request.method == "POST" and VAPI_SERVER_SECRET:
        incoming = request.headers.get("x-vapi-secret", "")
        if not hmac.compare_digest(incoming, VAPI_SERVER_SECRET):
            return JSONResponse(status_code=401, content={"error": "Unauthorized"})
    return await call_next(request)


app.include_router(availability.router)
app.include_router(appointments.router)
app.include_router(leads.router)
app.include_router(debug.router)
