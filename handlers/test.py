from aiogram import types

from keyboards import (audio_menu, back_photo_menu, home_menu, main_menu,
                       photo_menu)
from main import dp


async def send_audio(call, file, caption):
    await call.message.answer_photo(
            photo=open(file, 'rb'), caption=caption,
            reply_markup=back_photo_menu
        )
    await call.answer()


async def send_photo(call, file, caption):
    await call.message.answer_photo(
            photo=open(file, 'rb'), caption=caption,
            reply_markup=back_photo_menu
        )
    await call.answer()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Меня зовут Катя.", reply_markup=main_menu)


@dp.callback_query_handler(text='selfie')
async def send_selfie(call):
    await send_photo(call, 'IMG_6923.jpg', 'Это селфи!')


@dp.callback_query_handler(text='school_photo')
async def send_school_photo(call):
    await send_photo(call, 'IMG_6923.jpg', 'Это школьное фото!')


@dp.callback_query_handler(text='hobby')
async def send_post(call):
    await call.message.answer(text='История обо мне!', reply_markup=home_menu)
    await call.answer()


@dp.callback_query_handler(text='home')
async def send_menu(call):
    await call.message.answer(
        text='Что интересно узнать?', reply_markup=main_menu
    )
    await call.answer()


@dp.callback_query_handler(text='photo')
async def send_photo_menu(call):
    await call.message.answer(text='Галерея фото:', reply_markup=photo_menu)
    await call.answer()


@dp.callback_query_handler(text='audio')
async def send_audio_menu(call):
    await call.message.answer(
        text='Аудиорассказы обо всем:', reply_markup=audio_menu
    )
    await call.answer()
