import configparser

from middlewares import UserMiddleware

from aiogram import Bot, Router


config = configparser.ConfigParser()
config.read('config.ini')


# //////////// SETTINGS //////////////

token = config.get('SETTINGS', 'token')
bot = Bot(token=token, parse_mode='HTML')


# //////////// ROUTERS ////////////

user_router = Router()
user_router.message.outer_middleware(UserMiddleware())
