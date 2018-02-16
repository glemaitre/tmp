from compute import divide
from compute import multiply


def test_divide():
    x = divide(1, 2)
    assert x == 0.5


def test_multiply():
    x = multiply(2, 2)
    assert x == 4
