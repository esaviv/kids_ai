import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
