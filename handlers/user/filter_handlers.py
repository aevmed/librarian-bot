from main import user_router
from filters import IsNotAnEmptyBookList, IsNotAnEmptyMyBookList

from aiogram import types, F


# Обработчик фильтра списка книг
@user_router.message(IsNotAnEmptyMyBookList(), F.text == '🗑️ Удалить книгу')
async def delete_books_handler(message: types.Message):
    await message.answer('<b>⭕ К сожалению, список Ваших книг пуст :(</b>')


# Обработчик фильтра списка моих книг
@user_router.message(IsNotAnEmptyBookList(), F.text == '📃 Список всех книг')
async def filter_book_list_message_handler(message: types.Message):
    await message.answer('<b>⭕ К сожалению, список книг пуст :(</b>')

# Обработчик фильтра списка для поиска книг
@user_router.message(IsNotAnEmptyBookList(), F.text == '🔎 Поиск книги')
async def filter_find_book_message_handler(message: types.Message):
    await message.answer('<b>⭕ К сожалению, список книг пуст :(</b>')
