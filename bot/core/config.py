from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    bot_token: str = ''
    db_url: str = '"sqlite:///meditations.db"'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()