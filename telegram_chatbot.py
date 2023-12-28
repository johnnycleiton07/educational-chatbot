import telebot
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from unidecode import unidecode
from keyword_responder import KeywordResponder

nltk.download("punkt")
nltk.download("stopwords")

class TelegramBot:
    def __init__(self, token):
        self.TOKEN = token
        self.bot = telebot.TeleBot(self.TOKEN)
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words("portuguese"))
        self.keyword_responder = KeywordResponder()

        self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.bot.message_handler(func=lambda message: True)(self.handle_message)

    def preprocess_text(self, text):
        text = text.lower()
        text = unidecode(text)
        text = ''.join(c for c in text if c.isalnum() or c.isspace())

        tokens = nltk.word_tokenize(text)
        tokens = [token for token in tokens if token not in self.stop_words]

        tokens = [self.stemmer.stem(token) for token in tokens]

        preprocessed_text = ' '.join(tokens)
        return preprocessed_text

    def send_welcome(self, message):
        welcome_msg = "Digite sua mensagem, estou pronto para lhe ajudar! 🤖"
        self.bot.reply_to(message, welcome_msg)

    def handle_message(self, message):
        preprocessed_text = self.preprocess_text(message.text)
        response = self.keyword_responder.get_response(preprocessed_text)
        self.bot.reply_to(message, response)

    def start_polling(self):
        self.bot.polling()
