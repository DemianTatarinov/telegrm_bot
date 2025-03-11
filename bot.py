from telegram import Bot
import schedule
import time

TOKEN = '7810257621:AAGJaCdniU-1bphCkXV2wNFr-pJtIyqXBO8'
CHAT_ID = '161101736'
WORDS = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10"]

bot = Bot(token=TOKEN)

def send_words():
    bot.send_message(chat_id=CHAT_ID, text="\n".join(WORDS))

schedule.every().day.at("11:00").do(send_words)

while True:
    schedule.run_pending()
    time.sleep(1)
