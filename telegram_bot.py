import telebot
import os
import sys
import django
from pathlib import Path
from dotenv import load_dotenv
# подключаем django
BASE_DIR = str(Path(__file__).resolve().parent)

sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cryptocurrency.models import News, TelegramChannel, CryptoCurrency

# получаем ключ доступа к телегрвам боду из файла .env
load_dotenv()
BOT_API_HASH = os.environ['API_BOT_HASH']

bot = telebot.TeleBot(BOT_API_HASH, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "Welcome to News Crypto Currency Bot. Here you may ask about Crypto Currency News.\n\n/count - get cpount of news by crypto currency\n/latest - get 5 latest news by crypto currency.")

@bot.message_handler(commands=['count'])
def count_crypto_currecy_news(message):
    bot.reply_to(message, "Give me name of crypto currency.")
    bot.register_next_step_handler(message, get_news_count_by_name)

def get_news_count_by_name(message):
    name = message.text
    count = News.objects.filter(currencies__name__iexact=name).count()
    bot.reply_to(message, f"For crypto cyrrency {name} found {count} news.")


@bot.message_handler(commands=['latest'])
def show_top5_latest_news(message):
    bot.reply_to(message, "Give me name of crypto currency.")
    bot.register_next_step_handler(message, get_latest_news_by_name)

def get_latest_news_by_name(message):
    name = message.text
    news = News.objects.filter(currencies__name__iexact=name).order_by('-id')[:5]
    news_text = ''
    for item in news:
        news_text += item.text + "\n----------------------------\n"
    bot.reply_to(message, f"For crypto cyrrency {name} found: \n {news_text}")

if __name__ == '__main__':
    bot.infinity_polling()

