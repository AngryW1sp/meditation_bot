import random

from aiogram import F, Router
from aiogram.types import Message

from bot.utils.test_content import TEST_AFFIRMATIONS, TEST_MEDITATIONS, TEST_TIPS

router = Router()


@router.message(F.text == "Медитации")
async def send_meditation(message: Message):
    meditation_link = random.choice(TEST_MEDITATIONS)
    await message.answer(
        text=(
            "<b>Тестовая медитация</b>\n\n"
            f"Ссылка: {meditation_link}"
        )
    )


@router.message(F.text == "Аффирмации")
async def send_affirmation(message: Message):
    affirmation = random.choice(TEST_AFFIRMATIONS)
    await message.answer(
        text=(
            "<b>Тестовая аффирмация</b>\n\n"
            f"{affirmation}"
        )
    )


@router.message(F.text == "Советы")
async def send_tip(message: Message):
    tip = random.choice(TEST_TIPS)
    await message.answer(
        text=(
            "<b>Тестовый совет</b>\n\n"
            f"{tip}"
        )
    )