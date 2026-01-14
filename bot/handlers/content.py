import random

from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy import select

from bot.core.db import SessionLocal
from bot.models import Affirmation, Meditation, Tip
from bot.utils.test_content import TEST_AFFIRMATIONS, TEST_MEDITATIONS, TEST_TIPS
from bot.utils.text import SOS_TEXT

router = Router()


class ForMe(StatesGroup):
    choise_number = State()


@router.message(F.text == "🧘 Медитации")
async def send_meditation(message: Message):
    async with SessionLocal() as session:
        result = await session.execute(select(Meditation))
        items = result.scalars().all()
    if items:
        meditation = random.choice(items)
        await message.answer(text=(f"Ссылка: {meditation.link}"))
        return
    meditation_link = random.choice(TEST_MEDITATIONS)
    await message.answer(text=f"Ссылка: {meditation_link}")


@router.message(F.text == "💬 Аффирмации")
async def send_affirmation(message: Message):
    async with SessionLocal() as session:
        result = await session.execute(select(Affirmation))
        items = result.scalars().all()
    if items:
        affirmation = random.choice(items).text
    else:
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


@router.message(F.text == "💡 Советы")
async def send_tip(message: Message):
    async with SessionLocal() as session:
        result = await session.execute(select(Tip))
        items = result.scalars().all()
    if items:
        tip = random.choice(items).text
    else:
        tip = random.choice(TEST_TIPS)
    await message.answer(text=f"{tip}")


@router.message(F.text == "☀️ Проверь себя")
async def for_me(message: Message, state: FSMContext):
    await state.set_state(ForMe.choise_number)
    await message.answer(
        text="Как вы сейчас оцениваете свое настроение? Напишите цифру от 1 до 5"
    )


@router.message(ForMe.choise_number)
async def my_result(message: Message, state: FSMContext):
    user_text = (message.text or "").strip()

    # 1) Валидация: это число?
    if not user_text.isdigit():
        await message.answer("Пожалуйста, отправьте <b>цифру</b> от 1 до 5.")
        return

    rate = int(user_text)

    # 2) Валидация: число в диапазоне?
    if rate < 1 or rate > 5:
        await message.answer("Нужно число <b>от 1 до 5</b>. Попробуйте ещё раз.")
        return

    # 3) Ответы по диапазонам
    if rate in (1, 2):
        meditation_link = random.choice(TEST_MEDITATIONS)
        await message.answer(
            text=(
                "Спасибо, что делишься. Возможно, сейчас поможет короткая медитация.\n\n"
                f"Ссылка: {meditation_link}\n\n"
                "Береги себя."
            )
        )

    elif rate == 3:
        tip = random.choice(TEST_TIPS)
        await message.answer(
            text=(
                "Бывают такие дни. Может, небольшой совет?\n\n"
                f"💡 {tip}\n\n"
                "Если хочешь — могу отправить ещё один.Нажми «Советы» в меню — я подберу подходящий."
            )
        )

    else:  # 4 или 5
        await message.answer(
            text=(
                "Это здорово!\n"
                "Закрепи это состояние: сделай 3–5 осознанных вдохов, выдох чуть длиннее вдоха.\n\n"
                "Если захочешь — могу предложить короткую медитацию для поддержания."
                "Просто нажми 'Медитации'!"
            )
        )

    # 4) Завершаем сценарий
    await state.clear()

@router.message(F.text == "⛔ Помощь/Важно")
async def sos_help(message: Message):
    await message.answer(text=SOS_TEXT)