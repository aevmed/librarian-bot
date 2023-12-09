from main import user_router
from filters import IsNotAnEmptyBookList

from aiogram import types, F


@user_router.message(IsNotAnEmptyBookList(), F.text == '📃 Список всех книг')
async def filter_book_list_message_handler(message: types.Message):
    await message.answer('<b>⭕ К сожалению, список книг пуст :(</b>')