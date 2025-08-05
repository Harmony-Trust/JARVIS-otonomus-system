import logging

def check_quota(platform, sent_today):
    try:
        quota = platform.get("quota", 1)
        result = sent_today < quota
        if not result:
            logging.warning(f"Quota exceeded for {platform['name']}: {sent_today}/{quota}")
        return result
    except Exception as e:
        logging.error(f"Quota check error for {platform['name']}: {e}")
        return False

def check_policy(platform, content):
    try:
        policy = platform.get("policy", {})
        if "max_length" in policy and len(content) > policy["max_length"]:
            logging.warning(f"Content length exceeds policy for {platform['name']}")
            return False
        # ...tambahkan validasi lain...
        return True
    except Exception as e:
        logging.error(f"Policy check error for {platform['name']}: {e}")
        return False