from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6408678536:AAFcpf8CrHcnwlmajiZOtKrn60DP8KRCBW8')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    await message.answer('Hello')
    #await message.reply('Hello')

@dp.message_handler(commands=['inline'])
async def info(messge: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://www.youtube.com/watch?v=128u21Fn0TY&ab_channel=Rozetked'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await messge.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(callback_query.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    markup.add(types.KeyboardButton('site'))
    markup.add(types.KeyboardButton('website'))
    await message.answer('Hello', reply_markup=markup)


executor.start_polling(dp)