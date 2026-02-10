import orjson
from typing import Any


def process_payload(payload: dict[str, Any]) -> bytes:
    return orjson.dumps(payload, option=orjson.OPT_SORT_KEYS)
