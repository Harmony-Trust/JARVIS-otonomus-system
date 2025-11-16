# 🌐 JARVIS Module: main_api.py - FastAPI Gateway for Signup & Audit

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from signup import register_user
from supabase_client import init_supabase, store_platform_to_db
from audit_log import init_audit_logger, log_event
import logging

app = FastAPI(title="JARVIS API Gateway", version="2050.0")

# Inisialisasi koneksi saat startup
@app.on_event("startup")
def startup_event():
    init_supabase()
    init_audit_logger()
    logging.info("🚀 JARVIS API aktif dan siap menerima request.")

# Endpoint signup
@app.post("/signup")
async def signup_user(request: Request):
    data = await request.json()
    result = register_user(data)
    return JSONResponse(content=result)

# Endpoint platform distributor
@app.post("/platform")
async def add_platform(request: Request):
    data = await request.json()
    result = store_platform_to_db(data)
    log_event("main_api", "add_platform", {"name": data.get("name", "unknown")})
    return JSONResponse(content={"status": "success" if result else "error", "data": data})

# Endpoint audit log manual
@app.post("/audit")
async def manual_audit(request: Request):
    data = await request.json()
    log_event(data.get("source", "unknown"), data.get("action", "unknown"), data.get("detail", {}))
    return JSONResponse(content={"status": "logged"})
