from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.admin import admin_choise
from bot.utils.admin_access import is_admin

router = Router()


@router.message(Command('admin'))
async def open_admin(message: Message):
    if not is_admin(message.from_user.id):  # type: ignore
        await message.answer(text="Доступ к админ-панели ограничен.")
        return
    await message.answer(
        text="<b>Админ-панель</b>\n\nВыберите раздел:",
        reply_markup=admin_choise(),
    )
