from aiogram.utils.keyboard import InlineKeyboardBuilder


def choice_start_kb():
    start_kb = InlineKeyboardBuilder()
    start_kb.button(text="Catalog 🛒", callback_data="Catalog")
    start_kb.button(text="Registration", callback_data="Reg")
    start_kb.button(text="Log in", callback_data="Log")
    start_kb.adjust(2)
    return start_kb.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Choose one button",
    )
