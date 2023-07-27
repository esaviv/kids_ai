import logging
from aiogram import executor

from instance_bot import dp
from handlers import test

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
