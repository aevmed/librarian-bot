import math

from database import db

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def book_list_markup(page=1, items_per_page=5):
    builder = InlineKeyboardBuilder()

    book_list = db.get_book_list()

    start_item = (page - 1) * items_per_page
    end_item = start_item + 5

    for book in book_list[start_item:end_item]:
        builder.add(types.InlineKeyboardButton(text=f'{book.book_name} ({book.book_author})',
                                               callback_data=f'book:{book.id}:{page}'))

    builder.adjust(1)

    if len(book_list) <= 5:
        pass
    elif page == 1:
        builder.row(types.InlineKeyboardButton(text=f'{page} / {math.ceil(len(book_list) / items_per_page)}',
                                               callback_data='#'))
        builder.add(types.InlineKeyboardButton(text='>', callback_data=f'pg_next:{page}'))
    elif (page > 1) and (page < math.ceil(len(book_list) / items_per_page)):
        builder.row(types.InlineKeyboardButton(text=f'<', callback_data=f'pg_back:{page}'))
        builder.add(types.InlineKeyboardButton(text=f'{page} / {math.ceil(len(book_list) / items_per_page)}',
                                               callback_data='#'))
        builder.add(types.InlineKeyboardButton(text='>', callback_data=f'pg_next:{page}'))
    elif page == math.ceil(len(book_list) / items_per_page):
        builder.row(types.InlineKeyboardButton(text=f'<', callback_data=f'pg_back:{page}'))
        builder.add(types.InlineKeyboardButton(text=f'{page} / {math.ceil(len(book_list) / items_per_page)}',
                                               callback_data='#'))

    return builder.as_markup()


def book_markup(page):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(text='🔙 Назад',
                                           callback_data=f'back_to_book_list:{page}'))

    return builder.as_markup()
