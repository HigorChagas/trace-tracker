from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    ai_host: str = "http://localhost:11434/v1"


settings = Settings()
