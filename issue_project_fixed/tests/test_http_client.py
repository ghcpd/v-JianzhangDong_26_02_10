from app.http_client import APIClient


def test_client_creation():
    client = APIClient("https://example.com")
    assert client.client.base_url.host == "example.com"
