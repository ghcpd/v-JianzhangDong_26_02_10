from app.config import load_config

cfg = load_config()
print(cfg)
print(cfg.__dict__)
print('has api_base_url', hasattr(cfg, 'api_base_url'))
print('fields', list(cfg.__dict__.keys()))
