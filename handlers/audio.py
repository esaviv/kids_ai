from db.sqlite_db import get_content
from instance_bot import dp
from keyboards.user import audio_menu, back_audio_menu
from texts import MESSAGE_TEXTS


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
