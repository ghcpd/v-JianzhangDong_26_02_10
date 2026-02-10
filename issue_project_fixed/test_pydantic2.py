from pydantic import BaseModel

class AppConfig(BaseModel):
    api_base_url: str
    timeout: int = 5

config = AppConfig.parse_obj({'api_base_url':'https://example.com', 'timeout':5})
print(config)
print('api_base_url attr exists:', hasattr(config, 'api_base_url'))
print('api_base_url value:', getattr(config, 'api_base_url', None))
print('dict:', config.dict())
