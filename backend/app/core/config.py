from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Deriv Intelligence API"
    frontend_url: str = "http://localhost:3000"
    database_url: str = "sqlite+aiosqlite:///./deriv_intelligence.sqlite3"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "development-secret-change-me"
    access_token_minutes: int = 60
    deriv_app_id: str | None = None
    deriv_api_token: str | None = None

    email_host: str = "smtp.gmail.com"
    email_port: int = 587
    email_use_tls: bool = True
    email_host_user: str = ""
    email_host_password: str = ""
    default_from_email: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
