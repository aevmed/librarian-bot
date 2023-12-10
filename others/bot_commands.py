from aiogram import Bot

from aiogram.client.bot import BotCommand, BotCommandScopeDefault


# Списод команд юзера
user_commands = [
    BotCommand(command='start', description='📕 Перезапустить бота.'),
]


# Создаем команды
async def set_commands(bot: Bot):
    await bot.set_my_commands(commands=user_commands, scope=BotCommandScopeDefault())
