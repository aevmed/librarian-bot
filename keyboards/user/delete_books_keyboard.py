from database import db

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Разметка списка книг пользователя для удаления
def delete_books_markup(chat_id):
    builder = InlineKeyboardBuilder()

    my_book_list = db.get_my_book_list(chat_id)

    for my_book in my_book_list:
        builder.add(types.InlineKeyboardButton(text=f'{my_book.book_name} ({my_book.book_author})',
                                               callback_data=f'delete_book:{my_book.id}'))

    builder.adjust(2)

    return builder.as_markup()
