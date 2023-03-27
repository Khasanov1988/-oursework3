from utils.utils import load_json


def test_load_json():
    assert load_json('test') is None
    assert load_json('test_operations.json') == [1, 2, 3]
