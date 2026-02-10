from app.config import load_config, AppConfig


def test_load_config(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://example.com")
    config = load_config()
    assert isinstance(config, AppConfig)
