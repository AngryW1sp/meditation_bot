"""Модуль инициализации асинхронного подключения к базе данных.

Создаёт движок SQLAlchemy и фабрику сессий, а также предоставляет
зависимость `get_async_session` для использования в FastAPI.
"""

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from bot.core.config import settings
from bot.models import Base

engine = create_async_engine(settings.db_url, pool_pre_ping=True)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session
