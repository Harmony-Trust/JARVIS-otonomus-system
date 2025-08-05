# 🚀 Telegram Bot Integration

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from Alpha_Modular_Autopilot.brain_module.parser import parse_input

TELEGRAM_TOKEN = "your-telegram-bot-token"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("JARVIS Telegram Bot aktif!")

def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    result = parse_input(user_text)
    update.message.reply_text(f"Intent: {result['intent']}\nPlatforms: {result['platforms']}\nCategories: {result['categories']}")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()