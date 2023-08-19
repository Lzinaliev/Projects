import telebot
import sqlite3


name = None


bot = telebot.TeleBot('6408678536:AAFcpf8CrHcnwlmajiZOtKrn60DP8KRCBW8')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('xan.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегестрирую, введите ваше имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль!')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('xan.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('xan.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()      

    info = ''
    for i in users:
        info += f'Имя: {i[1]}, пароль:{i[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)



bot.polling(none_stop=True)