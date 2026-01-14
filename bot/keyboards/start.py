from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🧘 Медитации"),
                KeyboardButton(text="💬 Аффирмации"),
                KeyboardButton(text="💡 Советы"),
            ],
            [
                KeyboardButton(text="⛔ Помощь/Важно"),
                KeyboardButton(text="☀️ Проверь себя"),
            ],
            #[KeyboardButton(text="⏰ Уведомления")],
        ],
        resize_keyboard=True,
    )
    return kb
