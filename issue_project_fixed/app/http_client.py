import requests
from tenacity import retry, stop_after_attempt
from urllib.parse import urlparse
from types import SimpleNamespace


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        # Provide a simple client attribute with base_url having a host property
        parsed = urlparse(base_url)
        host = parsed.hostname
        # Create nested objects to mimic httpx.Client structure
        self.client = SimpleNamespace(base_url=SimpleNamespace(host=host))

    @retry(stop=stop_after_attempt(3))
    def get_status(self) -> int:
        response = requests.get(f"{self.base_url}/status")
        response.raise_for_status()
        return response.status_code
