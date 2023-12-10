import asyncio
import logging

from main import bot
from handlers import user_router
from others import set_commands
from database import db

from aiogram import Dispatcher

# Выполнение определенных функций прм запуске для функционирования юоь
async def on_startup():
    # Инициализация таблиц
    db.create_tables()
    
    # ///////////////////////

    # Создаем команды
    await set_commands(bot)


async def main():
    # Вызываем функцию
    await on_startup()
    
    # /////////////////////////

    # Объявление диспетчера
    dp = Dispatcher()
    
    # /////////////////////////

    # Маршрутизаторы
    dp.include_routers(user_router)
    
    # /////////////////////////

    # Выключаем обработку апдейтов, которые были пока бот спал
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
