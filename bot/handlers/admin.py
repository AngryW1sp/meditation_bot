from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.admin import admin_choice

router = Router()


@router.message(F.text == "Админ-панель")
async def open_admin(message: Message):
    await message.answer(
        text="<b>Админ-панель</b>\n\nВыберите раздел:",
        reply_markup=admin_choice(),
    )