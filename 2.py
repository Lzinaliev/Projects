import telebot


bot = telebot.TeleBot('')
id_chanel = '@WbTreasures41'

@bot.message_handler(content_types=['text'])
def commands(message):
    bot.send_message(id_chanel, message.text)


bot.polling(none_stop=True)