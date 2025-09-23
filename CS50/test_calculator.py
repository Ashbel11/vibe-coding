
from cal import squared


def test_squared():
    assert squared(2) == 4
    assert squared(3) == 9
def test_negative():
    assert squared(-2) == 4
def test_zero():
    assert squared(0) == 0

