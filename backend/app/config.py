from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Mini Task Management API"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./tasks.db"
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()


def is_sqlite() -> bool:
    return settings.DATABASE_URL.startswith("sqlite")
