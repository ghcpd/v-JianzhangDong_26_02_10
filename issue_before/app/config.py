from pydantic import BaseModel
from dotenv import dotenv_values


class AppConfig(BaseModel):
    api_base_url: str
    timeout: int = 5


def load_config() -> AppConfig:
    values = dotenv_values(".env")
    return AppConfig.model_validate(values)
