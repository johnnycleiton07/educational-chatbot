from telegram_bot import TelegramBot

#TOKEN = "6270004408:AAHiuivv6OT4u7AoQln4SQIUTo1zBsOP7UM"
TOKEN = "6594046226:AAEW9jo4hIS782S6-BX_-ToQV3Lad-oGJ-I"

if __name__ == "__main__":
    bot = TelegramBot(TOKEN)
    bot.start_polling()