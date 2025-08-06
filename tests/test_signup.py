# 👤 JARVIS Module: signup.py - Real User Registration & Audit Logging

import logging
from datetime import datetime
from supabase_client import init_supabase, store_payload
from audit_log import init_audit_logger, log_event

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Signup] %(message)s")

# Inisialisasi koneksi
init_supabase()
init_audit_logger()

def register_user(user_data: dict):
    if not isinstance(user_data, dict):
        logging.error("⚠️ Data user harus berupa dictionary.")
        return {"status": "error", "message": "Invalid data format"}

    # Validasi minimal
    required_fields = ["email", "name"]
    for field in required_fields:
        if field not in user_data:
            logging.error(f"❌ Field '{field}' wajib diisi.")
            return {"status": "error", "message": f"Missing field: {field}"}

    # Tambahkan metadata
    user_data["created_at"] = datetime.utcnow().isoformat()

    # Simpan ke Supabase
    result = store_payload("users", user_data)

    # Audit log
    log_event("signup", "register_user", {"email": user_data["email"], "status": "success" if result else "failed"})

    if result:
        logging.info(f"✅ User '{user_data['email']}' berhasil didaftarkan.")
        return {"status": "success", "data": user_data}
    else:
        return {"status": "error", "message": "Gagal menyimpan ke database"}
