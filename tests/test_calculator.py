import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(5, 3) == 5
    assert calc.add(6, 7) == 13

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.div(5, 0)

@pytest.mark.parametrize("a, b, result", [(2, 3, -1), (10, 5, 5)])
def test_subtract(calc, a, b, result):
    assert calc.sub(a, b) == result