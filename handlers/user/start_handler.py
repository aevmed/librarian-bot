from main import user_router
from keyboards import main_keyboard

from aiogram import types, filters


@user_router.message(filters.CommandStart())
async def start_command_handler(message: types.Message):
    await message.answer(text='<b>Привет!</b>👋\n\n'
                              '<i>Чтобы пользоваться ботом - используйте кнопки снизу.</i>',
                         reply_markup=main_keyboard())
