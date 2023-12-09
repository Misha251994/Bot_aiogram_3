from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# make menu in bot
async def command(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start work"),
        BotCommand(command="help", description="Help command"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
