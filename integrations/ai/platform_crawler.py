import requests
import logging
import json
import time

DEFAULT_QUOTA = 10
DEFAULT_POLICY = {
    "max_length": 500,
    "allowed_types": ["text"]
}
DEFAULT_STATUS = "❌ Belum daftar"

def crawl_platforms(retries=3, delay=5):
    found = []
    for attempt in range(retries):
        try:
            response = requests.get("https://public-directory.com/api/platforms")
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    # Filter hanya platform legal dan sesuai etika
                    if item.get("category") not in ["politics", "military"]:
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
                            "error_count": 0
                        }
                        found.append(platform)
                break
            else:
                logging.error(f"Failed to crawl platforms: {response.status_code}")
        except Exception as e:
            logging.error(f"Platform crawling error (attempt {attempt+1}): {e}")
            time.sleep(delay)
    return found

def update_platforms_json(new_platforms, path="platforms.json"):
    try:
        # Load existing platforms
        try:
            with open(path, "r", encoding="utf-8") as f:
                platforms = json.load(f)
        except FileNotFoundError:
            platforms = []
        # Merge, avoid duplicates by name
        existing_names = {p["name"] for p in platforms}
        for np in new_platforms:
            if np["name"] not in existing_names:
                platforms.append(np)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(platforms, f, ensure_ascii=False, indent=2)
        logging.info(f"Added {len(new_platforms)} new platforms to {path}")
    except Exception as e:
        logging.error(f"Failed to update platforms.json: {e}")

if __name__ == "__main__":
    new_platforms = crawl_platforms()
    if new_platforms:
        update_platforms_json(new_platforms)