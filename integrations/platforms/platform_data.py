import json
import logging

DEFAULT_QUOTA = 10
DEFAULT_POLICY = {
    "max_length": 500,
    "allowed_types": ["text"]
}
DEFAULT_STATUS = "❌ Belum daftar"

def validate_platform(item):
    required = ["name", "signup_url", "category"]
    for key in required:
        if key not in item or not item[key]:
            logging.warning(f"Platform missing '{key}': {item}")
            return False
    return True

def enrich_platform(p):
    p.setdefault("quota", DEFAULT_QUOTA)
    p.setdefault("policy", DEFAULT_POLICY)
    p.setdefault("status", DEFAULT_STATUS)
    p.setdefault("waktu", "")
    p.setdefault("last_signup", None)
    p.setdefault("last_distribute", None)
    p.setdefault("signup_attempts", 0)
    p.setdefault("distribute_count", 0)
    p.setdefault("error_count", 0)
    return p

def load_platforms(path="platforms.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            platforms = json.load(f)
        valid_platforms = []
        for p in platforms:
            p = enrich_platform(p)
            if validate_platform(p):
                valid_platforms.append(p)
        if len(valid_platforms) < len(platforms):
            logging.warning(f"{len(platforms) - len(valid_platforms)} invalid platforms skipped.")
        return valid_platforms
    except Exception as e:
        logging.error(f"Failed to load platforms: {e}")
        return []

# File ini hanya untuk data platform nyata dan aksi produksi.
# Semua pipeline signup, distribusi, dan monitoring gunakan load_platforms().