from app.config import load_config
print(load_config())
print(type(load_config()))
print(load_config().dict() if hasattr(load_config(), 'dict') else load_config().__dict__)
