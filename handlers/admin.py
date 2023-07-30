from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from db.sqlite_db import add_update_content
from instance_bot import ADMIN_ID, dp
from keyboards.admin import main_menu
from texts import MESSAGE_TEXTS


class FSMAdmin(StatesGroup):
    name = State()
    content = State()


@dp.message_handler(commands='admin', state=None)
async def add_new_content(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMAdmin.name.set()
        await message.answer(
            text=MESSAGE_TEXTS.get('add_new_content'), reply_markup=main_menu
        )


@dp.message_handler(
        text=[
            'selfie', 'school_photo', 'honeybee', 'hobby', 'gpt', 'sql', 'love'
        ],
        state=FSMAdmin.name
)
async def get_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await message.answer(
            text=MESSAGE_TEXTS.get('get_name'),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await FSMAdmin.next()


@dp.message_handler(
        content_types=['photo', 'voice', 'text'], state=FSMAdmin.content
)
async def save_content(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            if message.content_type == 'photo':
                data['content'] = message.photo[0].file_id
            elif message.content_type == 'voice':
                data['content'] = message.voice.file_id
            elif message.content_type == 'text':
                data['content'] = message.text
        await add_update_content(state)
        await message.answer(text=MESSAGE_TEXTS.get('save_content'))
        await state.finish()
