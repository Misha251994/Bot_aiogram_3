from aiogram.fsm.state import StatesGroup, State



class RegisterState(StatesGroup):
    reg_username = State()
    reg_email = State()
    reg_mb_phone = State()
    reg_password = State()