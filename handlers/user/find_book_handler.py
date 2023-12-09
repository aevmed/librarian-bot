from main import user_router

from aiogram import types, F


@user_router.message(F.text == '🔎 Поиск книги')
async def book_list_message_handler(message: types.Message):
    await message.answer('123')
