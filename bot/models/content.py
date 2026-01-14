from sqlalchemy import Integer, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.models.base import Base



class Meditation(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
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
