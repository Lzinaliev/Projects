import telebot
import requests
from bs4 import BeautifulSoup

token = ''
bot = telebot.TeleBot(token)

url = 'https://www.cnbc.com/technology/'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я бот для новостей. Введите команду /news, чтобы получить последние заголовки новостей из мира технологий.")

@bot.message_handler(commands=['news'])
def get_technology_news(message):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = soup.find_all('href', class_='Card-title')
            if headlines:
                news_headlines = [headline.text for headline in headlines]
                bot.send_message(message.chat.id, "Вот последние заголовки новостей из мира технологий:")
                for headline in news_headlines:
                    bot.send_message(message.chat.id, headline)
            else:
                bot.send_message(message.chat.id, "К сожалению, на данный момент не удалось найти заголовки новостей. Пожалуйста, попробуйте позже.")
        else:
            bot.send_message(message.chat.id, "К сожалению, не удалось получить новости в данный момент. Пожалуйста, попробуйте позже.")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при получении новостей. Пожалуйста, попробуйте позже.")

bot.polling()