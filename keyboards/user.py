from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from texts import BUTTONS

home_button = InlineKeyboardButton(
    text=BUTTONS.get('home'), callback_data='home'
)

main_menu = (
    InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(
            text=BUTTONS.get('photo_menu'), callback_data='photo_menu'
        ),
        InlineKeyboardButton(text=BUTTONS.get('hobby'), callback_data='hobby'),
        InlineKeyboardButton(text=BUTTONS.get('audio'), callback_data='audio'),
    )
)


photo_menu = (
    InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(
            text=BUTTONS.get('selfie'), callback_data='selfie'
        ),
        InlineKeyboardButton(
            text=BUTTONS.get('school_photo'), callback_data='school_photo'
        ),
        home_button
    )
)

audio_menu = (
    InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=BUTTONS.get('gpt'), callback_data='gpt'),
        InlineKeyboardButton(text=BUTTONS.get('sql'), callback_data='sql'),
        InlineKeyboardButton(text=BUTTONS.get('love'), callback_data='love'),
        home_button
    )
)


back_audio_menu = (
    InlineKeyboardMarkup().add(
        InlineKeyboardButton(text=BUTTONS.get('back'), callback_data='audio'),
        home_button
    )
)

back_photo_menu = (
    InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text=BUTTONS.get('back'), callback_data='photo_menu'
        ),
        home_button
    )
)

home_menu = (InlineKeyboardMarkup().add(home_button))
