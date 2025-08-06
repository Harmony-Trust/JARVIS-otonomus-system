# 📡 JARVIS Distribution Scheduler v2050 - Multi-Akun Celery Task Engine

from celery import Celery
from integrations.supabase.supabase_client import init_supabase, store_payload
from audit_log import init_audit_logger, log_event
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Scheduler] %(message)s")

# Inisialisasi koneksi
init_supabase()
init_audit_logger()

# Setup Celery
celery_app = Celery("jarvis_tasks", broker="redis://localhost:6379/0")

@celery_app.task(name="jarvis.distribute_multi_account")
def distribute_multi_account(payload: dict):
    if not isinstance(payload, dict) or "targets" not in payload:
        logging.error("⚠️ Payload harus berisi 'targets'.")
        return {"status": "error", "message": "Invalid multi-account payload"}

    results = []
    for target in payload["targets"]:
        entry = {
            "title": payload.get("title"),
            "category": payload.get("category"),
            "status": payload.get("status"),
            "platform": target.get("platform"),
            "account_id": target.get("account_id")
        }
        result = store_payload("distribution_logs", entry)
        log_event("distribution_scheduler", "distribute_multi_account", entry)
        results.append(result)

    logging.info(f"✅ Distribusi multi-akun selesai: {len(results)} akun")
    return {"status": "success", "distributed": len(results)}
