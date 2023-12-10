from database import db

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Разметка найденных книг по ключевому слову или фразе 
def found_books_markup(key_word):
    builder = InlineKeyboardBuilder()

    found_books = db.get_found_books_by_key_word(key_word)

    for found_book in found_books:
        builder.add(types.InlineKeyboardButton(text=f'{found_book.book_name} ({found_book.book_author})',
                                               callback_data=f'found_book:{found_book.id}'))

    builder.adjust(2)

    return builder.as_markup()
