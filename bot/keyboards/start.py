from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Медитации")],
            [KeyboardButton(text="Аффирмации")],
            [KeyboardButton(text="Советы")],
            [KeyboardButton(text="Уведомления")],
            [KeyboardButton(text="Админ-панель")],
        ], resize_keyboard=True
    )
    return kb
