import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

BUTTONS = {
    'selfie': 'Посмотреть моё последнее селфи',
    'school_photo': 'Посмотреть фото из старшей школы'
}

menu = (
    InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(
            text=BUTTONS.get('selfie'),
            callback_data='selfie'
        ),
        InlineKeyboardButton(
            text=BUTTONS.get('school_photo'),
            callback_data='school_photo'
        ),
    )
)

BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Меня зовут Катя.", reply_markup=menu)


@dp.callback_query_handler(text='selfie')
async def send_selfie(call):
    await call.message.answer_photo(
        photo=open('IMG_6923.jpg', 'rb'),
        caption=('Это селфи!')
    )
    await call.answer()


@dp.callback_query_handler(text='school_photo')
async def send_selfie(call):
    await call.message.answer_photo(
        photo=open('IMG_6923.jpg', 'rb'),
        caption=('Это школьное фото!')
    )
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)