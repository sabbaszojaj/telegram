from telegram.ext import Updater, CommandHandler
import os

# گرفتن توکن از متغیر محیطی
TOKEN = os.environ.get("BOT_TOKEN")

# تابع برای پاسخ به دستور /start
def start(update, context):
    update.message.reply_text("سلام! ربات زنده است و آماده پاسخگویی 😊")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # اضافه کردن هندلر برای دستور /start
    dp.add_handler(CommandHandler("start", start))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
