import telebot


bot = telebot.TeleBot('6156372105:AAGc5GnmGVqX_tocXejkDPB7IIFcn35fsas')
id_chanel = '@WbTreasures41'

@bot.message_handler(content_types=['text'])
def commands(message):
    bot.send_message(id_chanel, message.text)


bot.polling(none_stop=True)