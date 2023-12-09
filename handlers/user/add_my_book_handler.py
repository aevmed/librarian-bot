from main import user_router, bot
from states import BookStates
from keyboards import cancel_state_markup

from aiogram import types, F, filters
from aiogram.fsm.context import FSMContext


@user_router.message(F.text == '📌 Добавить свою книгу')
async def book_list_message_handler(message: types.Message, state: FSMContext):
    question = await message.answer(text='<b>🌼 Введите название книги!</b>', reply_markup=cancel_state_markup())

    await state.update_data(question_book_name_message_id=question.message_id)

    await state.set_state(BookStates.book_name)
