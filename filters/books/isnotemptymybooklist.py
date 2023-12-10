from database import db

from aiogram import filters, types


# Проверка списка моих книг
class IsNotAnEmptyMyBookList(filters.BaseFilter):
    async def __call__(self, message: types.Message, *args, **kwargs):
        chat_id = message.from_user.id

        my_book_list = db.get_my_book_list(chat_id)

        if len(my_book_list) == 0:
            return True
        else:
            return False
