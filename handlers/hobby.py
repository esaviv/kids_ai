from instance_bot import dp
from keyboards.user import home_menu
from texts import MESSAGE_TEXTS


@dp.callback_query_handler(text='hobby')
async def send_hobby(call):
    await call.message.answer(
        text=MESSAGE_TEXTS.get('hobby'), reply_markup=home_menu
    )
    await call.answer()
