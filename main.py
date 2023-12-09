import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TELEGRAM_USER_ID, Token
from app.database import models
from app.database.db_connect import init_db

# from handlers import base_handlers
# from utils.commands import command


async def start_bot(bot: Bot):
    # await init_db()
    # await command(bot)
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
    # dp.include_router(base_handlers.router)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot not work")
