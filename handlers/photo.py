from db.sqlite_db import get_content
from instance_bot import dp
from keyboards.user import back_photo_menu, photo_menu
from texts import MESSAGE_TEXTS


@dp.callback_query_handler(text=['selfie', 'school_photo'])
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
