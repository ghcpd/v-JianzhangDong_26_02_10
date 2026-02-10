import os

from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass
class AppConfig:
    api_base_url: str
    timeout: int = 5


def load_config() -> AppConfig:
    # Load values from .env file and override with environment variables
    values = {**dotenv_values(".env"), **os.environ}
    # Normalize keys to match AppConfig field names (snake_case)
    normalized = {k.lower(): v for k, v in values.items()}

    api_base_url = normalized.get("api_base_url", "")
    timeout = int(normalized.get("timeout", 5))

    return AppConfig(api_base_url=api_base_url, timeout=timeout)
