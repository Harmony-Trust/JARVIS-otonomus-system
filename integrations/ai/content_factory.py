# 🧠 JARVIS Content Factory v2050 - AI-Based Multi-Platform Generator

import openai
import logging
from audit_log import log_event
from auth import get_credentials

logging.basicConfig(level=logging.INFO, format="%(asctime)s [ContentFactory] %(message)s")

openai.api_key = get_credentials("openai_core")["api_key"]  # 🔐 Ambil dari auth.py

def generate_content(platform: dict, category: str, prompt: str = None):
    policy = platform.get("policy", {})
    max_length = policy.get("max_length", 500)
    allowed_types = policy.get("allowed_types", ["text"])
    content_type = allowed_types[0]

    if not prompt:
        prompt = f"Buat konten {category} untuk platform {platform['name']}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Anda adalah content creator profesional."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_length // 4
        )
        content = response.choices[0].message.content.strip()
        if len(content) > max_length:
            content = content[:max_length]

        logging.info(f"✅ Konten dibuat untuk {platform['name']}: {content[:50]}...")
        log_event("content_factory", "content_generated", {
            "platform": platform["name"],
            "category": category,
            "type": content_type,
            "length": len(content)
        })

        return {"type": content_type, "content": content}

    except Exception as e:
        logging.error(f"❌ Gagal generate konten untuk {platform['name']}: {e}")
        log_event("content_factory", "content_failed", {
            "platform": platform["name"],
            "category": category,
            "error": str(e)
        })
        return {"type": content_type, "content": ""}
