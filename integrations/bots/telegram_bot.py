# 🤖 JARVIS Module: Telegram Bot v2050 - Interaktif & Modular

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from Alpha_Modular_Autopilot.brain_module.parser import parse_input

logging.basicConfig(level=logging.INFO, format="%(asctime)s [TelegramBot] %(message)s")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Halo! JARVIS Telegram Bot aktif dan siap membantu.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    result = parse_input(user_text)
    reply = (
        f"🧠 Intent: {result.get('intent', 'unknown')}\n"
        f"📡 Platforms: {', '.join(result.get('platforms', []))}\n"
        f"🗂️ Categories: {', '.join(result.get('categories', []))}"
    )
    await update.message.reply_text(reply)

def main():
    if not TELEGRAM_TOKEN:
        logging.error("❌ TELEGRAM_TOKEN tidak ditemukan di environment.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("🚀 JARVIS Telegram Bot aktif.")
    app.run_polling()

if __name__ == "__main__":
    main()
