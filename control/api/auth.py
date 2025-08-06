# 🔐 JARVIS Auth v2050 - Multi-Account Credential Manager

from integrations.supabase.supabase_client import init_supabase, fetch_credentials
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Auth] %(message)s")

init_supabase()

def get_credentials(account_id: str):
    if not account_id:
        logging.warning("⚠️ account_id kosong.")
        return None

    creds = fetch_credentials("auth_accounts", account_id)
    if creds:
        logging.info(f"🔐 Kredensial ditemukan untuk: {account_id}")
        return creds
    else:
        logging.error(f"❌ Kredensial tidak ditemukan: {account_id}")
        return None

def list_all_accounts():
    accounts = fetch_credentials("auth_accounts")
    logging.info(f"📋 Total akun terdaftar: {len(accounts)}")
    return accounts
