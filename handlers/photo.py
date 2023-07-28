from instance_bot import dp
from keyboards.user import back_photo_menu, photo_menu
from texts import MESSAGE_TEXTS


async def send_photo(call, file, caption):
    await call.message.answer_photo(
            photo=open(file, 'rb'), caption=caption,
            reply_markup=back_photo_menu
        )
    await call.answer()


@dp.callback_query_handler(text='selfie')
async def send_selfie(call):
    await send_photo(call, 'IMG_6923.jpg', MESSAGE_TEXTS.get('selfie'))


@dp.callback_query_handler(text='school_photo')
async def send_school_photo(call):
    await send_photo(call, 'IMG_6923.jpg', MESSAGE_TEXTS.get('school_photo'))


@dp.callback_query_handler(text='photo_menu')
async def send_photo_menu(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('photo_menu'), reply_markup=photo_menu
    )
    await call.answer()
