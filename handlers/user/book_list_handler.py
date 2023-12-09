from main import user_router
from database import db
from filters import IsNotAnEmptyBookList

from aiogram import types, F


@user_router.message(F.text == '📃 Список всех книг')
async def book_list_message_handler(message: types.Message):
    await message.answer('123')
