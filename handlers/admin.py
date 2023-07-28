from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from instance_bot import ADMIN_ID, dp
from keyboards.admin import main_menu


class FSMAdmin(StatesGroup):
    name = State()
    content = State()


@dp.message_handler(commands='admin', state=None)
async def send_welcome(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMAdmin.name.set()
        await message.answer(
            text='Что хочешь обновить?', reply_markup=main_menu
        )


@dp.message_handler(
        commands=['selfie', 'school_photo', 'hobby', 'gpt', 'sql', 'love'],
        state=FSMAdmin.name
)
async def add_new(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['name'] = message.text[1:]
        await message.answer(text='Загрузи контент:')
        await FSMAdmin.next()


@dp.message_handler(
        content_types=['photo', 'voice', 'text'], state=FSMAdmin.content
)
async def add_content(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            if message.content_type == 'photo':
                await message.answer(text=f'photo: {message.photo[0].file_id}')
                data['content'] = message.photo[0].file_id
            elif message.content_type == 'voice':
                await message.answer(text=f'voice: {message.voice.file_id}')
                data['content'] = message.voice.file_id
            elif message.content_type == 'text':
                await message.answer(text=f'text: {message.text}')
                data['content'] = message.text
        await state.finish()
