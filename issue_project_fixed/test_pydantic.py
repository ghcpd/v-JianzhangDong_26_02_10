from pydantic import BaseModel

class AppConfig(BaseModel):
    api_base_url: str
    timeout: int = 5

print(AppConfig.parse_obj({'api_base_url':'https://example.com', 'timeout':5}))
print(AppConfig.parse_obj({'api_base_url':'https://example.com'}))
print(AppConfig.parse_obj({'timeout':5}))
