from app.processor import process_payload


def test_process_payload():
    data = {"b": 1, "a": 2}
    result = process_payload(data)
    assert result == b'{"a":2,"b":1}'
