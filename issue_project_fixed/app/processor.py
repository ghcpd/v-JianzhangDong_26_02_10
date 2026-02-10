import json
from typing import Any


def process_payload(payload: dict[str, Any]) -> bytes:
    # Use standard library json to avoid external Rust dependencies
    return json.dumps(payload, sort_keys=True, separators=(',', ':')).encode('utf-8')
