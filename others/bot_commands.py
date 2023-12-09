from aiogram import Bot

from aiogram.client.bot import BotCommand, BotCommandScopeDefault


user_commands = [
    BotCommand(command='start', description='📕 Перезапустить бота.'),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands=user_commands, scope=BotCommandScopeDefault())
