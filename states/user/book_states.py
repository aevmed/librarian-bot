from main import user_router, bot, genre_list
from keyboards import main_markup, cancel_state_markup, book_genres_markup
from database import db

from aiogram import types, filters, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class BookStates(StatesGroup):
    book_name = State()
    book_author = State()
    book_description = State()
    book_genre = State()
    book_my_genre = State()


@user_router.message(BookStates.book_name)
async def book_name_state(message: types.Message, state: FSMContext):
    book_name = message.text

    question = await message.answer(text='<b>✍️ Кто являеся автором этой книги?</b>', reply_markup=cancel_state_markup())

    await state.update_data(book_name=book_name, question_book_author_message_id=question.message_id)

    await state.set_state(BookStates.book_author)


@user_router.message(BookStates.book_author)
async def book_author_state(message: types.Message, state: FSMContext):
    book_author = message.text

    question = await message.answer(text='<b>📝 Напишите описание Вашей книги!</b>', reply_markup=cancel_state_markup())

    await state.update_data(book_author=book_author, question_book_description_message_id=question.message_id)

    await state.set_state(BookStates.book_description)


@user_router.message(BookStates.book_description)
async def book_description_state(message: types.Message, state: FSMContext):
    book_description = message.text

    question = await message.answer(text='<b>🎭 Выберите жанр Вашей книги!</b>', reply_markup=book_genres_markup())

    await state.update_data(book_description=book_description, question_book_jenre_message_id=question.message_id)

    await state.set_state(BookStates.book_genre)


@user_router.callback_query(F.data == 'cancel_state', filters.StateFilter('*'))
async def cancel_state_callback_handler(callback: types.CallbackQuery, state: FSMContext):
    check_state = await state.get_state()

    if check_state is None:
        await callback.answer('Вы ничего не вводите.')
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)
    else:
        await callback.message.answer(text='<b>❌ Вы отменили процесс добавления книги!</b>', reply_markup=main_markup())

        data = await state.get_data()

        message_ids_with_markup = [
            data.get('question_book_name_message_id'),
            data.get('question_book_author_message_id'),
            data.get('question_book_description_message_id'),
            data.get('question_book_jenre_message_id'),
            data.get('question_my_genre_message_id'),
        ]

        for message_id_with_markup in message_ids_with_markup:
            try:
                await bot.edit_message_reply_markup(reply_markup=None, chat_id=callback.from_user.id,
                                                    message_id=message_id_with_markup)
            except:
                continue

        await state.clear()


@user_router.message(F.text == '🔙 Отмена', filters.StateFilter('BookStates:book_genre'))
async def cancel_state_message_handler(message: types.Message, state: FSMContext):
    await message.answer(text='<b>❌ Вы отменили процесс добавления книги!</b>', reply_markup=main_markup())

    await state.clear()


@user_router.message(BookStates.book_genre)
async def book_genre(message: types.Message, state: FSMContext):
    if message.text in genre_list:
        book_genre = message.text
        data = await state.get_data()

        book_name = data.get('book_name')
        book_author = data.get('book_author')
        book_description = data.get('book_description')

        db.add_book(book_name, book_author, book_description, book_genre, message.from_user.id)

        await message.answer(text='<b>✅ Ваша книга добавлена в список книг :)</b>', reply_markup=main_markup())

        message_ids_with_markup = [
            data.get('question_book_name_message_id'),
            data.get('question_book_author_message_id'),
            data.get('question_book_description_message_id'),
            data.get('question_book_jenre_message_id'),
        ]

        await state.clear()

        for message_id_with_markup in message_ids_with_markup:
            try:
                await bot.edit_message_reply_markup(reply_markup=None, chat_id=message.from_user.id,
                                                    message_id=message_id_with_markup)
            except:
                continue
    elif message.text == 'Ввести самому жанр':
        question = await message.answer(text='<b>👩🏼‍🎤 Введите название своего жанра! </b>',
                                        reply_markup=cancel_state_markup())

        await state.update_data(question_my_genre_message_id=question.message_id)

        await state.set_state(BookStates.book_my_genre)
    else:
        await message.answer(text='<b>❌ Я Вас не понял, выберите жанр, либо отмените процесс добавления книги :)</b>',
                             reply_markup=book_genres_markup())
        return


@user_router.message(BookStates.book_my_genre)
async def book_my_genre_state(message: types.Message, state: FSMContext):
    book_my_genre = message.text

    data = await state.get_data()

    book_name = data.get('book_name')
    book_author = data.get('book_author')
    book_description = data.get('book_description')

    db.add_book(book_name, book_author, book_description, book_my_genre, message.from_user.id)

    await message.answer(text='<b>✅ Ваша книга добавлена в список книг :)</b>', reply_markup=main_markup())

    message_ids_with_markup = [
        data.get('question_book_name_message_id'),
        data.get('question_book_author_message_id'),
        data.get('question_book_description_message_id'),
        data.get('question_book_jenre_message_id'),
        data.get('question_my_genre_message_id'),
    ]

    await state.clear()

    for message_id_with_markup in message_ids_with_markup:
        try:
            await bot.edit_message_reply_markup(reply_markup=None, chat_id=message.from_user.id,
                                                message_id=message_id_with_markup)
        except:
            continue
