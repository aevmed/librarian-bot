from main import user_router

from aiogram import types, F


@user_router.message(F.text == '📌 Добавить свою книгу')
async def book_list_message_handler(message: types.Message):
    await message.answer('123')
