# 📊 JARVIS Quota & Policy Engine v2050 - Multi-Platform Validator

import logging
from audit_log import log_event

def check_quota(platform: dict, sent_today: int) -> bool:
    try:
        quota = platform.get("quota", 1)
        result = sent_today < quota
        if not result:
            logging.warning(f"⚠️ Quota exceeded: {platform['name']} {sent_today}/{quota}")
            log_event("quota_policy", "quota_exceeded", {
                "platform": platform["name"],
                "sent_today": sent_today,
                "quota": quota
            })
        return result
    except Exception as e:
        logging.error(f"❌ Quota check error: {platform['name']} | {e}")
        return False

def check_policy(platform: dict, content: str, content_type: str = "text") -> bool:
    try:
        policy = platform.get("policy", {})
        max_length = policy.get("max_length", 500)
        allowed_types = policy.get("allowed_types", ["text"])

        if len(content) > max_length:
            logging.warning(f"⚠️ Konten terlalu panjang: {len(content)}/{max_length}")
            log_event("quota_policy", "policy_violation", {
                "platform": platform["name"],
                "issue": "length_exceeded",
                "length": len(content),
                "max_length": max_length
            })
            return False

        if content_type not in allowed_types:
            logging.warning(f"⚠️ Tipe konten tidak diizinkan: {content_type}")
            log_event("quota_policy", "policy_violation", {
                "platform": platform["name"],
                "issue": "type_not_allowed",
                "type": content_type,
                "allowed": allowed_types
            })
            return False

        return True
    except Exception as e:
        logging.error(f"❌ Policy check error: {platform['name']} | {e}")
        return False
