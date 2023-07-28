from instance_bot import dp
from keyboards.user import audio_menu, back_audio_menu


async def send_audio(call, file, caption):
    await call.message.answer_audio(
            audio=open(file, 'rb'), caption=caption,
            reply_markup=back_audio_menu
        )
    await call.answer()


@dp.callback_query_handler(text='audio')
async def send_audio_menu(call):
    await call.message.answer(
        text='Аудиорассказы обо всем:', reply_markup=audio_menu
    )
    await call.answer()


@dp.callback_query_handler(text='gpt')
async def send_audio_gpt(call):
    await send_audio(call, 'audio_2023-07-28_10-39-37.ogg', 'gpt!')


@dp.callback_query_handler(text='sql')
async def send_audio_sql(call):
    await send_audio(call, 'audio_2023-07-28_10-39-37.ogg', 'sql!')


@dp.callback_query_handler(text='love')
async def send_audio_love(call):
    await send_audio(call, 'audio_2023-07-28_10-39-37.ogg', 'love!')
