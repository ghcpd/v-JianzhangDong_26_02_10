from pydantic import BaseModel

class AppConfig(BaseModel):
    api_base_url: str
    timeout: int = 5

print('fields', AppConfig.__fields__)
print('schema', AppConfig.schema())

config = AppConfig.parse_obj({'api_base_url':'https://example.com', 'timeout':5})
print('config dict', config.dict())
print('config', config)
