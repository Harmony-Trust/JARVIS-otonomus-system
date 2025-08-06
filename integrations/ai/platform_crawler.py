# 🌐 JARVIS Platform Crawler v2050 - Legal & Ethical Platform Collector

import requests
import logging
import json
import time

DEFAULT_QUOTA = 10
DEFAULT_POLICY = {
    "max_length": 500,
    "allowed_types": ["text", "video", "image"]
}
DEFAULT_STATUS = "❌ Belum daftar"

EXCLUDED_CATEGORIES = ["politics", "military", "gambling", "adult"]

def crawl_platforms(retries=3, delay=5):
    found = []
    for attempt in range(retries):
        try:
            response = requests.get("https://public-directory.com/api/platforms")
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    if item.get("category") not in EXCLUDED_CATEGORIES:
                        platform = {
                            "name": item.get("name"),
                            "signup_url": item.get("signup_url"),
                            "category": item.get("category", "general"),
                            "quota": DEFAULT_QUOTA,
                            "policy": DEFAULT_POLICY,
                            "status": DEFAULT_STATUS,
                            "waktu": "",
                            "last_signup": None,
                            "last_distribute": None,
                            "signup_attempts": 0,
                            "distribute_count": 0,
                            "error_count": 0,
                            "accounts": []  # 🧠 Multi-akun siap ditambahkan
                        }
                        found.append(platform)
                break
            else:
                logging.error(f"❌ Gagal crawl: {response.status_code}")
        except Exception as e:
            logging.error(f"⚠️ Error crawling (attempt {attempt+1}): {e}")
            time.sleep(delay)
    return found

def update_platforms_json(new_platforms, path="platforms.json"):
    try:
        try:
            with open(path, "r", encoding="utf-8") as f:
                platforms = json.load(f)
        except FileNotFoundError:
            platforms = []

        existing_names = {p["name"] for p in platforms}
        added = 0
        for np in new_platforms:
            if np["name"] not in existing_names:
                platforms.append(np)
                added += 1

        with open(path, "w", encoding="utf-8") as f:
            json.dump(platforms, f, ensure_ascii=False, indent=2)

        logging.info(f"✅ {added} platform baru ditambahkan ke {path}")
    except Exception as e:
        logging.error(f"❌ Gagal update {path}: {e}")

if __name__ == "__main__":
    new_platforms = crawl_platforms()
    if new_platforms:
        update_platforms_json(new_platforms)
