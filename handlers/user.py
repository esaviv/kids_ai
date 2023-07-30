from aiogram import types

from db.sqlite_db import get_content
from instance_bot import dp
from keyboards.user import (audio_menu, back_audio_menu, back_photo_menu,
                            home_menu, main_menu, photo_menu)
from texts import MESSAGE_TEXTS


@dp.message_handler(commands=['start', 'home'])
async def send_welcome(message: types.Message):
    await message.answer(
        text=MESSAGE_TEXTS.get('main_menu'), reply_markup=main_menu
    )


@dp.callback_query_handler(text='home')
async def send_main_menu(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('main_menu'), reply_markup=main_menu
    )
    await call.answer()


@dp.callback_query_handler(text=['selfie', 'school_photo', 'honeybee'])
async def send_photo(call):
    await call.message.answer_photo(
            photo=await get_content(call.data),
            reply_markup=back_photo_menu
        )
    await call.answer()


@dp.callback_query_handler(text='photo_menu')
async def send_photo_menu(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('photo_menu'), reply_markup=photo_menu
    )
    await call.answer()


@dp.callback_query_handler(text='hobby')
async def send_hobby(call):
    await call.message.answer(
        text=await get_content(call.data), reply_markup=home_menu
    )
    await call.answer()


@dp.callback_query_handler(text=['gpt', 'sql', 'love'])
async def send_audio(call):
    await call.message.answer_audio(
            audio=await get_content(call.data),
            reply_markup=back_audio_menu
        )
    await call.answer()


@dp.callback_query_handler(text='audio')
async def send_audio_menu(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('audio_menu'), reply_markup=audio_menu
    )
    await call.answer()
