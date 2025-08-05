import openai
import logging
import random

openai.api_key = "your-openai-api-key"

def generate_content(platform, category, prompt=None):
    policy = platform.get("policy", {})
    max_length = policy.get("max_length", 500)
    allowed_types = policy.get("allowed_types", ["text"])
    content_type = allowed_types[0]

    if not prompt:
        prompt = f"Buat konten {category} untuk platform {platform['name']}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Anda adalah content creator profesional."},
                      {"role": "user", "content": prompt}],
            max_tokens=max_length // 4  # approx 4 chars per token
        )
        content = response.choices[0].message.content.strip()
        if len(content) > max_length:
            content = content[:max_length]
        logging.info(f"Generated content for {platform['name']}: {content[:50]}...")
        return {"type": content_type, "content": content}
    except Exception as e:
        logging.error(f"AI content generation failed for {platform['name']}: {e}")
        return {"type": content_type, "content": ""}

# Test
if __name__ == "__main__":
    platform = {"name": "facebook", "policy": {"max_length": 500, "allowed_types": ["text"]}}
    print(generate_content(platform, "promo"))