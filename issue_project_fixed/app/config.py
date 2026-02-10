from pydantic import BaseModel, ConfigDict, Field
from dotenv import dotenv_values


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)
    
    api_base_url: str = Field(alias="API_BASE_URL")
    timeout: int = Field(default=5, alias="TIMEOUT")


def load_config() -> AppConfig:
    values = dotenv_values(".env")
    return AppConfig.model_validate(values)
