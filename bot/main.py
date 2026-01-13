import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.core.config import settings

from bot.handlers.start import router as start_router
from bot.handlers.admin import router as admin_router
from bot.handlers.content import router as content_router


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.include_router(start_router)
    dp.include_router(admin_router)
    dp.include_router(content_router)
    await dp.start_polling(bot)  # type: ignore


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот завершил свою работу!")
