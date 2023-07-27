from keyboards import (audio_menu, back_photo_menu, home_menu, main_menu,
                       photo_menu)
from main import dp

async def send_photo(call, file, caption):
    await call.message.answer_photo(
            photo=open(file, 'rb'), caption=caption,
            reply_markup=back_photo_menu
        )
    await call.answer()