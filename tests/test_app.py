from app import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    # Intentional error for demo
    assert multiply(2, 3) == 5
