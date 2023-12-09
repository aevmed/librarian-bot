from main import user_router

from aiogram import types, filters


@user_router.message(filters.CommandStart())
async def start_command_handler(message: types.Message):
    await message.answer('123')
