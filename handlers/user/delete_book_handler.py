from main import user_router, bot
from keyboards import delete_books_markup
from database import db

from aiogram import types, F


# Обработчик удаления своих книг
@user_router.message(F.text == '🗑️ Удалить книгу')
async def book_list_message_handler(message: types.Message):
    chat_id = message.from_user.id

    await message.answer(text='<b>🗑️ Выберите книгу, которую хотите удалить.</b>',
                         reply_markup=delete_books_markup(chat_id))


# Обработчик нажатия на книгу из списка
@user_router.callback_query(F.data.startswith('delete_book'))
async def delete_book_callback_handler(callback: types.CallbackQuery):
    callback_data = callback.data

    chat_id =callback.from_user.id

    book_id = callback.data.split(':')[1]

    db.delete_book(book_id)

    await callback.answer('Книга была удалена.')

    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=delete_books_markup(chat_id))

    if len(db.get_my_book_list(chat_id)) == 0:
        await callback.message.edit_text(text='<b> Вы удалили все книги! </b>')
