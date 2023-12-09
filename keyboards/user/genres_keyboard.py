from main import genre_list

from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def book_genres_markup():
    builder = ReplyKeyboardBuilder()

    for genre in genre_list:
        builder.add(types.KeyboardButton(text=genre))

    builder.adjust(2)

    builder.row(types.KeyboardButton(text='Ввести самому жанр'))

    builder.row(types.KeyboardButton(text='🔙 Отмена'))

    return builder.as_markup(resize_keyboard=True)
