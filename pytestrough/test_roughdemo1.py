import pytest

def test_value_divisble_by_5(init_driver):
    assert init_driver % 5 == 0
