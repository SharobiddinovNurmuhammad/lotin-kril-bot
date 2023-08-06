import logging

from config import API_TOKEN
from aiogram import  Bot, Dispatcher, executor, types
from functions import editText


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Lotin-Kril Botga xush kelibsiz!')

@dp.message_handler()
async def lotinKril(message: types.Message):
    text = message.text
    msg = await editText(text)
    await message.answer(msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)