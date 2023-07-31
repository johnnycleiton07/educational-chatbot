from telegram_bot import TelegramBot

TOKEN = "6270004408:AAHiuivv6OT4u7AoQln4SQIUTo1zBsOP7UM"

if __name__ == "__main__":
    bot = TelegramBot(TOKEN)
    bot.start_polling()