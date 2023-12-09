import configparser

from middlewares import UserMiddleware

from aiogram import Bot, Router


config = configparser.ConfigParser()
config.read('config.ini', 'utf-8')


# //////////// SETTINGS //////////////

token = config.get('SETTINGS', 'token')
bot = Bot(token=token, parse_mode='HTML')


genres = config.get('SETTINGS', 'genres')

genre_list = []

for genre in genres.split(','):
    genre_list.append(genre)

# //////////// ROUTERS ////////////

user_router = Router()
user_router.message.outer_middleware(UserMiddleware())
