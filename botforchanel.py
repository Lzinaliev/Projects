import telebot
from telebot import types

bot = telebot.TeleBot('6156372105:AAGc5GnmGVqX_tocXejkDPB7IIFcn35fsas')
id_chanel = '@WbTreasures41'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить', callback_data='continue'))
    bot.send_message(message.id_chanel, 'Привет, жми кнопку, чтобы продолжить', reply_markup=markup)

#@bot.callback_query_handler(func=lambda callback:True)
#def callback_message(callback):
    #if callback.data == 'continue':
        #bot.send_message(callback.message.id_chanel, 'Hello')


bot.polling(none_stop=True)