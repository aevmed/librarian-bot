from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Разметка кнопки отмены состояния машины
def cancel_state_markup():
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(text='🔙 Отмена', callback_data='cancel_state'))

    return builder.as_markup()
