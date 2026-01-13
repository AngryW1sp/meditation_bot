from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str = ""
    # Async SQLAlchemy URL (SQLite)
    db_url: str = "sqlite+aiosqlite:///./meditations.db"
    admin_ids: str = ""
    # Scheduler settings (local time)
    timezone: str = "Europe/Belgrade"
    morning_meditation_time: str = "08:00"
    tip_day_time: str = "12:00"
    tip_evening_time: str = "18:00"
    evening_meditation_time: str = "21:00"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
