# 📡 JARVIS Content Distributor v2050 - Multi-Akun, Multi-Platform Engine

import logging
from integrations.platforms.platforms_data import load_platforms
from integrations.ai.content_factory import generate_content
from control.harmony.quota_policy_engine import check_quota, check_policy
from audit_log import log_event

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Distributor] %(message)s")

def distribute_all(category: str, sent_today_dict: dict):
    platforms = load_platforms()
    for platform in platforms:
        for account_id in platform.get("accounts", []):
            sent_today = sent_today_dict.get(account_id, 0)

            for _ in range(platform["quota"]):
                if not check_quota(platform, sent_today):
                    break

                content_obj = generate_content(platform, category)
                content = content_obj["content"]
                content_type = content_obj["type"]

                if not check_policy(platform, content, content_type):
                    continue

                try:
                    # Simulasi distribusi (API call, post, dsb)
                    logging.info(f"🚀 Distribusi ke {platform['name']} - {account_id}: {content[:50]}...")
                    log_event("distributor", "content_sent", {
                        "platform": platform["name"],
                        "account_id": account_id,
                        "category": category,
                        "length": len(content)
                    })
                    sent_today += 1
                except Exception as e:
                    logging.error(f"❌ Distribusi gagal: {platform['name']} - {account_id} | {e}")
                    log_event("distributor", "distribution_failed", {
                        "platform": platform["name"],
                        "account_id": account_id,
                        "error": str(e)
                    })

if __name__ == "__main__":
    distribute_all("promo", {})
