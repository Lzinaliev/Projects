import telebot
from telebot import types

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Define the channel IDs
channel_id1 = -1001707086519  # Replace with the ID of your first channel
channel_id2 = -1001962601108  # Replace with the ID of your second channel

# Track users who clicked "Confirm" button
confirmed_users = set()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("🔎 Найти фильм", callback_data='find_movie')
    markup.add(button)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'find_movie')
def handle_callback(call):
    if call.data == 'find_movie':
        user_id = call.message.chat.id
        send_subscription_check(user_id)

def send_subscription_check(chat_id):
    subscribed_channel1 = check_subscription(chat_id, channel_id1)
    subscribed_channel2 = check_subscription(chat_id, channel_id2)
    if subscribed_channel1 and subscribed_channel2:
        send_message_after_subscription_check(chat_id)
    else:
        markup = types.InlineKeyboardMarkup(row_width=2)  # Set row_width to 2 for two columns
        sponsor1_button = types.InlineKeyboardButton("Спонсор №1", url='https://t.me/WbTreasures41')
        sponsor2_button = types.InlineKeyboardButton("Спонсор №2", url='https://t.me/CoinTraderPro15')
        confirm_button = types.InlineKeyboardButton("Подтвердить", callback_data='confirm')
        markup.add(sponsor1_button, sponsor2_button)
        markup.add(confirm_button)  # Add the confirm button in a separate row
        bot.send_message(chat_id, "Сначала вам нужно подписаться на оба канала", reply_markup=markup)


def send_message_after_subscription_check(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)  # Set row_width to 2 for two columns
    sponsor1_button = types.InlineKeyboardButton("Спонсор №1", url='https://t.me/WbTreasures41')
    sponsor2_button = types.InlineKeyboardButton("Спонсор №2", url='https://t.me/CoinTraderPro15')
    confirm_button = types.InlineKeyboardButton("Подтвердить✅", callback_data='confirm')
    markup.add(sponsor1_button, sponsor2_button)
    markup.add(confirm_button)  # Add the confirm button in a separate row
    bot.send_message(chat_id, "Прежде чем воспользоваться ботом, подпишитесь на наших спонсоров и нажмите кнопку \"Подтвердить✅\", чтобы продолжить.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'confirm')
def handle_confirm_callback(call):
    user_id = call.message.chat.id
    confirmed_users.add(user_id)
    bot.answer_callback_query(call.id, "Вы подтвердили свое решение. Проверяем подписки...")
    subscribed_channel1 = check_subscription(user_id, channel_id1)
    subscribed_channel2 = check_subscription(user_id, channel_id2)
    if subscribed_channel1 and subscribed_channel2:
        bot.send_message(user_id, "Вы успешно подписались! \nВведите код фильма в формате: 123")
    else:
        bot.send_message(user_id, "Не удалось проверить подписку на спонсоров, попробуйте снова.")

@bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 3)
def handle_code_message(message):
    user_id = message.chat.id
    if user_id in confirmed_users:
        code = message.text
        if code == '001':
            with open('fix.py', 'rb') as f:
                bot.send_document(user_id, f, caption="Файл для кода: {}".format(code))
        else:
            bot.send_message(user_id, "Неверный код. Попробуйте еще раз.")
    else:
        bot.send_message(user_id, "Для получения файла необходимо сначала подтвердить свое решение и выполнить требуемые действия.")	



# Function to check user's subscription to channels
def check_subscription(user_id, channel_id):
    try:
        chat_member = bot.get_chat_member(channel_id, user_id)  # Check if the user is a member of the channel
        return chat_member.status == 'member' or chat_member.status == 'creator'
    except telebot.apihelper.ApiException:
        return False


bot.polling()