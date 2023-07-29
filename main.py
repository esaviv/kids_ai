import logging
import sys

from aiogram import executor

from db.sqlite_db import start_sql
from handlers import admin, user
from instance_bot import dp

async def on_startup(_):
    start_sql()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
