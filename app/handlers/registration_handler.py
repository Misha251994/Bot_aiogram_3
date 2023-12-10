from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from app.states.registration_state import RegisterState
from app.utils.check_utils import is_valid_email, is_valid_phone_number

register_router = Router()


@register_router.callback_query(F.data == "Registration")
async def start_register(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        f"Let's start registration 📝 Enter your name, please: "
    )
    await state.set_state(RegisterState.reg_username)


@register_router.message(RegisterState.reg_username, F.text)
async def add_username(message: Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer("Name can't include only number")
        await message.answer("Enter your name, please: ")
        await state.set_state(RegisterState.reg_username)
    else:
        await state.update_data(username=message.text)
        await message.answer(" Great👌 Now let's add your email: ")
        await state.set_state(RegisterState.reg_email)


@register_router.message(RegisterState.reg_email, F.text)
async def add_email(message: Message, state: FSMContext):
    if is_valid_email(message.text):
        await state.update_data(email=message.text)
        await message.answer(
            "Your email is correct 💯 It's time to write your mobile phone number📲: "
        )
        await state.set_state(RegisterState.reg_mb_phone)
    else:
        await message.answer("Your email is not valid🥺 Try again please!")
        await state.set_state(RegisterState.reg_email)


@register_router.message(RegisterState.reg_mb_phone, F.text)
async def add_mb_phone(message: Message, state: FSMContext):
    if is_valid_phone_number(message.text):
        await state.update_data(mb_phone=message.text)
        await message.answer(
            "😊 Good job! A little bit left, let's create a secret password🔐"
        )
        await state.set_state(RegisterState.reg_password)
    else:
        await message.answer(" Maybe you forgot phone number😅 Try again!")
        await state.set_state(RegisterState.reg_mb_phone)


@register_router.message(RegisterState.reg_password, F.text)
async def add_password(message: Message, state: FSMContext):
