import logging
from integrations.platforms.platform_data import load_platforms
from integrations.ai.content_factory import generate_content
from control.harmony.quota_policy_engine import check_quota, check_policy

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Distributor] %(message)s")

def distribute_all(category, sent_today_dict):
    platforms = load_platforms()
    for platform in platforms:
        sent_today = sent_today_dict.get(platform["name"], 0)
        for _ in range(platform["quota"]):
            if not check_quota(platform, sent_today):
                break
            content_obj = generate_content(platform, category)
            content = content_obj["content"]
            if not check_policy(platform, content):
                continue
            # Simulasi distribusi (API call, post, dsb)
            try:
                logging.info(f"Distributing to {platform['name']}: {content[:50]}...")
                # ...implementasi distribusi...
                sent_today += 1
            except Exception as e:
                logging.error(f"Distribution failed for {platform['name']}: {e}")

if __name__ == "__main__":
    distribute_all("promo", {})