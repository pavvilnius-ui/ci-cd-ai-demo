# app.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0

# New functions
def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus by zero")
    return a % b

def is_positive(n):
    return n > 0
