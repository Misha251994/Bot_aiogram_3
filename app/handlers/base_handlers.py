from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import Bot

from app.keyboards.inline_kb import choice_start_kb
from app.utils.commands import command

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        f"Hello {(message.from_user.full_name)}!✋, I'm Avocado, exotic fruits sales bot!\n\n"
        "You can buy everything you want from the list\n\n"
        "Click on the command <b>Catalog 🛒</b>\n\n"
        "But first <b>you need to register</b>,"
        "otherwise the other commands will not be available!\n\n"
        "Click on <b>Registration ✌️</b> or <b>Log in 👋</b>",
        reply_markup=choice_start_kb(),
    )
    await command(bot)


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
