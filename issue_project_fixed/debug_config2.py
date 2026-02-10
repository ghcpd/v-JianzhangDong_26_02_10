from dotenv import dotenv_values
import os

values = {**dotenv_values('.env'), **os.environ}
print('raw values', values)
normalized = {k.lower(): v for k, v in values.items()}
print('normalized', normalized)
from app.config import load_config, AppConfig
print(load_config())
