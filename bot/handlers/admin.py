from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.admin import admin_choise
from bot.utils.text import ADMIN_PANEL_TEXT

router = Router()


@router.message(F.text == "Админ-панель")
async def open_admin(message: Message):
    await message.answer(text=ADMIN_PANEL_TEXT, reply_markup=admin_choise())
