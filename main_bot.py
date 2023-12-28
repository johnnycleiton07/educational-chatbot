from telegram_chatbot import TelegramBot

def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

if __name__ == "__main__":
    token_file_path = 'token.txt'
    TOKEN = read_token_from_file(token_file_path)

    bot = TelegramBot(TOKEN)
    bot.start_polling()