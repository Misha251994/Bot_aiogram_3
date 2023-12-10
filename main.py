import asyncio
import logging
from typing import Text

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers import router_list
from app.handlers.registration_handler import start_register
from app.utils.commands import command
from config import TELEGRAM_USER_ID, Token


async def start_bot(bot: Bot):
    # await init_db()
    await command(bot)
    await bot.send_message(TELEGRAM_USER_ID, text="Bot start")


async def stop_bot(bot: Bot):
    await bot.send_message(TELEGRAM_USER_ID, text="Bot stop ")
    await bot.close()


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=Token, parse_mode="HTML")
    dp.include_routers(*router_list)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot not work")
