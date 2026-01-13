"""Модуль инициализации асинхронного подключения к базе данных.

Создаёт движок SQLAlchemy и фабрику сессий, а также предоставляет
зависимость `get_async_session` для использования в FastAPI.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from collections.abc import AsyncIterator

from bot.core.config import settings

engine = create_async_engine(settings.db_url, pool_pre_ping=True)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_async_session() -> AsyncIterator:  # type: ignore
    """Асимптотическая генератор-зависимость, отдающая сессию.

    Используется в `Depends` для внедрения `AsyncSession` в обработчики.
    """
    async with SessionLocal() as session:
        yield session
