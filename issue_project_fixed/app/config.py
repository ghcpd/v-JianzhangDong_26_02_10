from pydantic import BaseModel
from dotenv import dotenv_values
import os


class AppConfig(BaseModel):
    api_base_url: str
    timeout: int = 5


def load_config() -> AppConfig:
    # Load from .env file and environment variables
    from pathlib import Path

    # Determine project root from this file's location
    BASE_DIR = Path(__file__).resolve().parent.parent

    raw = dotenv_values(BASE_DIR / ".env") or {}
    merged = {**raw}
    # Override with environment variables
    for key, val in os.environ.items():
        if key in ["API_BASE_URL", "TIMEOUT"]:
            merged[key] = val

    # Map to model field names
    config_data: dict[str, any] = {}
    if "API_BASE_URL" in merged:
        config_data["api_base_url"] = merged["API_BASE_URL"]
    if "TIMEOUT" in merged:
        config_data["timeout"] = merged["TIMEOUT"]

    return AppConfig(**config_data)
