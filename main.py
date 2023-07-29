#from aiogram import executor
from aiogram.utils.executor import start_webhook

from db.sqlite_db import start_sql
from handlers import admin, user
from instance_bot import dp, bot, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST, WEBHOOK_PATH, WEBHOOK_URL

async def on_startup(_):
    start_sql()
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
