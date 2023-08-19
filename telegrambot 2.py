import telebot
from telebot import types

bot = telebot.TeleBot("6679473191:AAG2TUz6Sb92doBDGH4R5CLkDfgyHYTBxNw")

#рвбота с инлайн кнопками, их размешение и т.д
@bot.message_handler(content_types='photo')
def user_photo(message):
    markup = types.InlineKeyboardMarkup()
    #сами кнопки
    btn1 = types.InlineKeyboardButton('перейти на сайт', url="https://www.invokergame.com/")
    btn2 = types.InlineKeyboardButton( 'удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton( 'изменить текст', callback_data='edit')
    #функция которая добавляет кнопки
    markup.row(btn1)
    markup.row(btn2,btn3)
    #бот отвечает на сообщение юзера
    bot.reply_to(message, 'Какое красивое фото!', reply_markup = markup)

#функция которая считывает делит или эдит и в зависимости от нажатой кнопки делает действие
@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif  callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
