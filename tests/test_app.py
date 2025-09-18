# tests/test_app.py

from app import add, multiply, subtract, divide, is_even, power, modulus, is_positive
import pytest

# ---- Addition tests ----
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# ---- Multiplication tests ----
def test_multiply():
    # Intentional fail for demo
    assert multiply(2, 3) == 5

# ---- Subtraction tests ----
def test_subtract():
    assert subtract(5, 3) == -2
    assert subtract(0, 4) == 4

# ---- Division tests ----
def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)  # test divide by zero

# ---- Even number tests ----
def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False

# ---- Power tests ----
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 1) == 3

# ---- Modulus tests ----
def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(9, 3) == 0
    with pytest.raises(ValueError):
        modulus(5, 0)

# ---- Is Positive tests ----
def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-1) is False
    assert is_positive(0) is False
