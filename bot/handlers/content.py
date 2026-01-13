import random

from aiogram import F, Router
from aiogram.types import Message

from bot.utils.test_content import TEST_AFFIRMATIONS, TEST_MEDITATIONS, TEST_TIPS

router = Router()


@router.message(F.text == "Медитации")
async def send_meditation(message: Message):
    meditation_link = random.choice(TEST_MEDITATIONS)
    await message.answer(text=(f"Ссылка: {meditation_link}"))


@router.message(F.text == "Аффирмации")
async def send_affirmation(message: Message):
    affirmation = random.choice(TEST_AFFIRMATIONS)
    await message.answer(
        text=(
            f"{affirmation}\n\n"
            "<b>Как повторять аффирмации:</b>\n"
            "• Выберите одну фразу на день и повторяйте 3–5 минут.\n"
            "• Дышите спокойно и произносите слова в настоящем времени.\n"
            "• Подкрепляйте фразу действием: маленький шаг = большой эффект."
        )
    )


@router.message(F.text == "Советы")
async def send_tip(message: Message):
    tip = random.choice(TEST_TIPS)
    await message.answer(text=(f"{tip}"))
