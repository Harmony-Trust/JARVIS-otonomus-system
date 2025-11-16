# 📜 JARVIS Module: Audit Logger v2050 - Aktivitas & Transparansi Sistem

import os
import logging
from datetime import datetime
from supabase import create_client, Client

logging.basicConfig(level=logging.INFO, format="%(asctime)s [AuditLog] %(message)s")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = None

def init_audit_logger():
    global supabase
    if not SUPABASE_URL or not SUPABASE_KEY:
        logging.error("❌ Supabase credentials tidak ditemukan.")
        return None
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        logging.info("✅ Audit logger terhubung ke Supabase.")
        return supabase
    except Exception as e:
        logging.error(f"❌ Gagal inisialisasi audit logger: {e}")
        return None

def log_event(source: str, action: str, detail: dict = None):
    if not supabase:
        logging.error("❌ Audit logger belum diinisialisasi.")
        return None
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "action": action,
        "detail": detail or {}
    }
    try:
        response = supabase.table("audit_logs").insert(payload).execute()
        logging.info(f"📝 Audit log disimpan: {source} - {action}")
        return response
    except Exception as e:
        logging.error(f"❌ Gagal menyimpan audit log: {e}")
        return None
