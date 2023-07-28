from aiogram import types

from instance_bot import dp
from keyboards.user import main_menu
from texts import MESSAGE_TEXTS


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        text=MESSAGE_TEXTS.get('welcome'), reply_markup=main_menu
    )


@dp.callback_query_handler(text='home')
async def send_main_menu(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('main_menu'), reply_markup=main_menu
    )
    await call.answer()
