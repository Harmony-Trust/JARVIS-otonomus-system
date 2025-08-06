# 📣 JARVIS Module: Telegram Notifier v2050 - Real-Time Alert System

import os
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Notifier] %(message)s")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        logging.error("❌ Telegram credentials tidak ditemukan di environment.")
        return None

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            logging.info("📨 Alert Telegram berhasil dikirim.")
        else:
            logging.warning(f"⚠️ Gagal kirim alert: {response.text}")
        return response
    except Exception as e:
        logging.error(f"❌ Error saat kirim alert: {e}")
        return None
