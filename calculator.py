#https://github.com/camiladleong/lab-11-CD-MA.git
#Partner 1: Camila D' Leon
#Partner 2: Muhammad Athar

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(base, value):
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for logarithm")
    if value <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(value, base)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)
