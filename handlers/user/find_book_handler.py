from main import user_router
from states import BookStates

from aiogram import types, F
from aiogram.fsm.context import FSMContext


# Обработчик поиска книги
@user_router.message(F.text == '🔎 Поиск книги')
async def book_list_message_handler(message: types.Message, state: FSMContext):
    await message.answer('<b>📨 Введите Ваш запрос для поиска книги по базе данных! </b>')

    await state.set_state(BookStates.find_book_by_key_word)
