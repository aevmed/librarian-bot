from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard():
    builder = ReplyKeyboardBuilder()

    markups = [
        types.KeyboardButton(text='📃 Список всех книг'),
        types.KeyboardButton(text='🔎 Поиск книги'),
        types.KeyboardButton(text='📌 Добавить свою книгу'),
        types.KeyboardButton(text='🗑️ Удалить книгу')
    ]

    for markup in markups:
        builder.add(markup)

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
