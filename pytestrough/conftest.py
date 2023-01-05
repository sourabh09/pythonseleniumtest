import pytest

@pytest.fixture()
def init_driver():
    value = 100
    return value

