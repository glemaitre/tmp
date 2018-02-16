import pytest
import numpy as np

from compute import divide
from compute import multiply


@pytest.mark.parametrize(
    "lop, rop, res",
    [(1, 2, 0.5),
     (1, 0, np.inf)]
)
def test_divide(lop, rop, res):
    x = divide(lop, rop)
    assert x == pytest.approx(res)


def test_multiply():
    x = multiply(2, 2)
    assert x == 4
