from main import user_router
from database import db
from keyboards import book_list_markup, book_markup

from aiogram import types, F


@user_router.message(F.text == '📚 Список всех книг')
async def book_list_message_handler(message: types.Message):
    await message.answer(text='<b>📚 Список загруженных книг</b>',
                         reply_markup=book_list_markup())


@user_router.callback_query(F.data.startswith('book'))
async def book_callback_handler(callback: types.CallbackQuery):
    await callback.answer('')

    callback_data = callback.data

    book_id = callback_data.split(':')[1]
    page = callback.data.split(':')[2]

    book_info = db.get_book(book_id)

    await callback.message.edit_text(text=f'<b>🌼 Название книги: {book_info.book_name}</b>\n'
                                          f'<b>✍️ Автор книги: {book_info.book_author}</b>\n'
                                          f'<b>🎭 Жанр книги: {book_info.book_genre}</b>\n\n'
                                          f'<b>📝 Описание книги:\n{book_info.book_description}</b>',
                                     reply_markup=book_markup(page))


@user_router.callback_query(F.data.startswith('back_to_book_list'))
async def back_to_book_list_callback_handler(callback: types.CallbackQuery):
    await callback.answer('')

    callback_data = callback.data

    page = int(callback_data.split(':')[1])

    await callback.message.edit_text(text='<b>📚 Список загруженных книг</b>',
                                     reply_markup=book_list_markup(page=page))


@user_router.callback_query(F.data.startswith('pg_next'))
async def pagination_next_callback_handler(callback: types.CallbackQuery):
    await callback.answer('')

    callback_data = callback.data

    page = int(callback_data.split(':')[1])

    await callback.message.edit_reply_markup(reply_markup=book_list_markup(page=page + 1))


@user_router.callback_query(F.data.startswith('pg_back'))
async def pagination_back_callback_handler(callback: types.CallbackQuery):
    await callback.answer('')

    callback_data = callback.data

    page = int(callback_data.split(':')[1])

    await callback.message.edit_reply_markup(reply_markup=book_list_markup(page=page - 1))
