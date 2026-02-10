import sys
sys.path.insert(0,'issue_project_fixed')
from app.config import AppConfig

try:
    cfg = AppConfig()
    print('created', cfg)
    print(cfg.model_dump())
except Exception as e:
    print('error', type(e), e)
