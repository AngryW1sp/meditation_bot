from aiogram.utils.keyboard import InlineKeyboardBuilder


def notifications_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Включить", callback_data="notify_on")
    kb.button(text="Выключить", callback_data="notify_off")
    kb.adjust(2)
    return kb.as_markup()