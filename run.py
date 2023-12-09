import asyncio

from main import bot
from handlers import user_router
from others import set_commands
from database import db

from aiogram import Dispatcher


async def on_startup():
    db.create_tables()
    # ///////////////////////
    await set_commands(bot)


async def main():
    await on_startup()
    # /////////////////////////
    dp = Dispatcher()
    # /////////////////////////
    dp.include_routers(user_router)
    # /////////////////////////
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
