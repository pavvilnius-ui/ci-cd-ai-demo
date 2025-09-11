# tests/test_app.py

from app import add, multiply, subtract, divide, is_even
import pytest

# ---- Addition tests ----
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# ---- Multiplication tests ----
def test_multiply():
    # Intentional fail for demo
    assert multiply(2, 3) == 5 # should be 6

# ---- Subtraction tests ----
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

# ---- Division tests ----
def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)  # test divide by zero

# ---- Even number tests ----
def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
