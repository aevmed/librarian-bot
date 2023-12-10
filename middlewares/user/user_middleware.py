from database import db

from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


# Обрабатываем каждый апдейт от человека и добавляем в бд, если его нет
class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        chat_id = event.from_user.id
        username = event.from_user.username

        check_user = db.check_user(chat_id)

        if check_user:
            return await handler(event, data)
        else:
            db.add_user(chat_id, username)
            return await handler(event, data)
