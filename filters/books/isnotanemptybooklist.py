from database import db

from aiogram import filters, types


class IsNotAnEmptyBookList(filters.BaseFilter):
    async def __call__(self, *args, **kwargs):
        book_list = db.get_book_list()

        if len(book_list) == 0:
            return True
        else:
            return False
