from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler

TOKEN = '7810257621:AAGJaCdniU-1bphCkXV2wNFr-pJtIyqXBO8'

def start(update: Update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(f"Ваш chat_id: {chat_id}")

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
