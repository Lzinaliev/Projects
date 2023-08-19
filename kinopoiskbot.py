import telebot
from telebot import types
from kinopoisk.movie import Movie

TOKEN = '6425047705:AAHNSoNs317zOA0hX0ClLReGNvWc-6ngvRY'
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("🔎 Найти фильм", callback_data='find_movie')
    markup.add(button)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'find_movie')
def handle_callback(call):
    user_id = call.message.chat.id
    bot.send_message(user_id, "Введите название фильма:")
    bot.register_next_step_handler(call.message, process_movie_name)

def process_movie_name(message):
    user_id = message.chat.id
    movie_name = message.text
    movie_id = find_movie_id(movie_name)
    if movie_id:
        bot.send_message(user_id, f"Фильм '{movie_name}' найден на Кинопоиске.")
        watch_link = f"https://www.kinopoisk.gg/film/{movie_id}"
        markup = types.InlineKeyboardMarkup()
        watch_button = types.InlineKeyboardButton("Смотреть онлайн", url=watch_link)
        markup.add(watch_button)
        bot.send_message(user_id, "Ссылка на просмотр фильма:", reply_markup=markup)
    else:
        bot.send_message(user_id, f"Фильм с названием '{movie_name}' не найден на Кинопоиске.")

def find_movie_id(movie_name):
    try:
        movies = Movie.objects.search(movie_name)
        if movies:
            return movies[0].id
    except:
        pass 
    return None

bot.polling()
