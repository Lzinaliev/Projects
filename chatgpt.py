import logging
import openai
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Уровень логирования
logging.basicConfig(level=logging.INFO)

# Установите ваш токен GPT-3.5
openai.api_key = ''

# Создание экземпляра бота и диспетчера
bot = Bot(token='')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Функция для генерации ответа с помощью GPT-3.5
async def generate_response(message: str) -> str:
    prompt = f"User: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот, готовый для общения.")

# Обработка текстовых сообщений
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
    user_message = message.text
    response = await generate_response(user_message)
    formatted_response = md.text(md.bold("AI:"), md.code(response))
    await message.reply(formatted_response, parse_mode=types.ParseMode.MARKDOWN)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
