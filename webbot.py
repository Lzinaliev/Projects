from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6408678536:AAFcpf8CrHcnwlmajiZOtKrn60DP8KRCBW8')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open website', web_app=WebAppInfo(url='https://hd.kinopoisk.ru/')))
    await message.answer('Hello my friend!', reply_markup = markup)

executor.start_polling(dp)