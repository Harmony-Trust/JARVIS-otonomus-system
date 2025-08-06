# 🚀 JARVIS Module: Supabase Integration v2050 - Secure & Reliable

import os
import logging
from supabase import create_client, Client

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Supabase] %(message)s")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = None

def init_supabase():
    global supabase
    if not SUPABASE_URL or not SUPABASE_KEY:
        logging.error("❌ Supabase credentials tidak ditemukan di environment variables.")
        return None
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        logging.info("✅ Supabase client berhasil diinisialisasi.")
        return supabase
    except Exception as e:
        logging.error(f"❌ Gagal inisialisasi Supabase: {e}")
        return None

def store_payload(table: str, data: dict):
    if not supabase:
        logging.error("❌ Supabase belum diinisialisasi.")
        return None
    if not isinstance(data, dict):
        logging.error("⚠️ Data payload harus berupa dictionary.")
        return None
    try:
        response = supabase.table(table).insert(data).execute()
        logging.info(f"📦 Payload disimpan di '{table}': {data}")
        return response
    except Exception as e:
        logging.error(f"❌ Gagal menyimpan payload: {e}")
        return None

def store_platform_to_db(platform: dict):
    if not supabase:
        logging.error("❌ Supabase belum diinisialisasi.")
        return None
    try:
        response = supabase.table("platforms").insert(platform).execute()
        logging.info(f"🧩 Platform disimpan: {platform.get('name', 'Unknown')}")
        return response
    except Exception as e:
        logging.error(f"❌ Gagal menyimpan platform: {e}")
        return None
