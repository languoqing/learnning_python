import pytest


@pytest.fixture()
def a():
    return 5

#@pytest.mark.usefixtures("a")
def test_b(a):
    re = a
    assert re == 5
