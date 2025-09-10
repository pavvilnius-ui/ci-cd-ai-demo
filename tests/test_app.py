from app import add, multiply

def test_add():
    assert add(2, 3) == 5  # will pass

def test_multiply():
    print("test Multiply")
    assert multiply(2, 3) == 6  # intentional fail for demo (expected 6)
