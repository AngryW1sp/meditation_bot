from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy import select

from bot.core.db import SessionLocal
from bot.keyboards.start import start_kb
from bot.models.user_settings import UserSettings
from bot.utils.text import WELCOME_TEXT

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    async with SessionLocal() as session:
        result = await session.execute(
            select(UserSettings).where(UserSettings.user_id == message.from_user.id)  # type: ignore
        )

        if not result.scalar_one_or_none():
            user = UserSettings(user_id=message.from_user.id)  # type: ignore
            session.add(user)
            await session.commit()

    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=start_kb(),
    )
