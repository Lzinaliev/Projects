import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
	mess = f'Привет, {message.from_user.first_name}'
	bot.send_message(message.chat.id, mess,)

@bot.message_handler(content_types=['text'])
def user_text(message):
	if message.text == 'hello':
		bot.send_message(message.chat.id, "и тебе привет",)
	elif message.text == "video":
		video = open('3.mp4', 'rb')
		bot.send_video(message.chat.id, video)
	else:
		bot.send_message(message.chat.id,'я тебя не понимаю')

@bot.message_handler(content_types=['photo'])
def user_photo(message):
	bot.send_message(message.chat.id, "вау, крутое фото!")

@bot.message_handler(commands=['website'])
def website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить веб сайт", url= 'https://ais.ninja/'))
	bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)




bot.polling(none_stop=True)

