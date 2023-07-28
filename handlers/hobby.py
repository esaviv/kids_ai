from db.sqlite_db import get_content
from instance_bot import dp
from keyboards.user import home_menu


@dp.callback_query_handler(text='hobby')
async def send_hobby(call):
    await call.message.answer(
        text=await get_content(call.data), reply_markup=home_menu
    )
    await call.answer()
