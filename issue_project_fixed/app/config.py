from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    api_base_url: str
    timeout: int = 5


def load_config() -> AppConfig:
    return AppConfig()
