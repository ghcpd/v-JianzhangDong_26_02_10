import httpx
from tenacity import retry, stop_after_attempt


class APIClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(base_url=base_url)

    @retry(stop=stop_after_attempt(3))
    def get_status(self) -> int:
        response = self.client.get("/status")
        response.raise_for_status()
        return response.status_code
