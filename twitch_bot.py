import telebot
from bs4 import BeautifulSoup
import requests
from telebot import types

TOKEN = ''  
bot = telebot.TeleBot(TOKEN)
url = "https://www.twitch.tv/xaney96"
streamer = url

def is_online():
        url = streamer
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, features="html.parser")
        script_tags = soup.find_all("script", type="application/ld+json")
        is_live = False
        for script in script_tags:
            try:
                data = script.string
                if '"isLiveBroadcast":true' in data:
                    is_live = True
                    break
            except Exception as e:
                print(f"Ошибка при парсинге JSON-LD: {e}")
        return is_live


@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text=" CHECK", callback_data="check")
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Я сообщу, когда начнётся стрим!",reply_markup=keyboard)
    

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    callback.message.chat.id = '-1001707086519'
    n = is_online()
    if callback.data == 'check':
        if n:
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="GO", url=streamer)
            keyboard.add(button1)
            bot.send_message(callback.message.chat.id,"Стрим в прямом эфире!",reply_markup=keyboard)
        else:
            keyboard1 = types.InlineKeyboardMarkup()
            button2 = types.InlineKeyboardButton(text="YT", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            button3 = types.InlineKeyboardButton(text="VK", url="https://vk.com/durov?from=search")
            button4 = types.InlineKeyboardButton(text="X", url="https://x.com/realDonaldTrump")
            keyboard1.add(button2,button3,button4)
        
            bot.send_message(callback.message.chat.id,"Стрим не в прямом эфире.",reply_markup=keyboard1)


  
@bot.message_handler(commands=['admin'])
def start(message):
    bot.send_message(message.chat.id, "Enter password")


bot.polling(True)