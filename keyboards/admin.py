from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = (
    ReplyKeyboardMarkup(row_width=2).add(
        KeyboardButton(text='selfie'),
        KeyboardButton(text='school_photo'),
        KeyboardButton(text='honeybee'),
        KeyboardButton(text='hobby'),
        KeyboardButton(text='gpt'),
        KeyboardButton(text='sql'),
        KeyboardButton(text='love'),
    )
)
