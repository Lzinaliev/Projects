import telebot
from telebot import types
from pytube import YouTube
import os



bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('продолжить', callback_data= 'continue' ))
    bot.send_message(message.chat.id, 'Привет, этот бот скачает любое видео из ютуб! Нажимай кнопку продолжить.', reply_markup=markup )

@bot.callback_query_handler(func=lambda calback:True)
def callback_message(callback):
    if callback.data == 'continue':
        bot.send_message(callback.message.chat.id, 'Введите ссылку на видео:')

@bot.message_handler()
def link_text(message):
    try:
        link = message.text
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        # Получение размера видео
        video_size = video.filesize
        # Скачивание видео
        video.download(output_path='', filename='2.mp4')
        # Отправка сообщения о начале скачивания
        bot.send_message(message.chat.id, "Видео началось скачиваться...")
        # Ожидание, пока файл полностью скачается
        while os.path.getsize('2.mp4') != video_size:
            pass
        # Отправка видео пользователю
        with open('2.mp4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)
        # Удаление временного файла
        os.remove('2.mp4')

    except Exception as e:
        bot.reply_to(message, "Ошибка при скачивании видео: " + str(e))

bot.polling(none_stop=True)