import logging

from aiogram import executor

from db.sqlite_db import start_sql
from handlers import admin, audio, hobby, home, photo
from instance_bot import dp

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    start_sql()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
