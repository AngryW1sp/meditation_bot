from enum import Enum
from sqlalchemy import Integer, Text, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SAEnum

from bot.models.base import Base


class TimeEnum(str, Enum):
    MORNING = "morning"
    EVENING = "evening"
    UNIVERSAL = "universal"


class Meditation(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    time: Mapped[TimeEnum] = mapped_column(
        SAEnum(TimeEnum, name="meditation_time_enum"),
        nullable=False,
        default=TimeEnum.UNIVERSAL,
    )

    # пример поля со ссылкой, раз у вас медитации — ссылки
    link: Mapped[str] = mapped_column(String(2048), nullable=False)

    # необязательное описание
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)


class Affirmation(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)


class Tip(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
