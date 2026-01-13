from sqlalchemy import BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from bot.models.base import Base


class UserSettings(Base):
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
