from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Медитации")],
            [KeyboardButton(text="Аффирмации")],
            [KeyboardButton(text="Советы")],
            [KeyboardButton(text="Админ-панель")],
        ]
    )
    return kb
