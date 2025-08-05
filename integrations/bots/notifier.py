import requests

TELEGRAM_TOKEN = "your-telegram-token"
CHAT_ID = "your-chat-id"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)