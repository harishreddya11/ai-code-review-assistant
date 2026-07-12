from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DevPilot AI"
    app_version: str = "1.0.0"
    debug: bool = True

    llm_provider: str = "openai"

    openrouter_api_key: str = ""
    openrouter_model: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()