"""
Explain method overloading and overriding in python
"""

def addition(a, b):
    return a + b

def addition(a, b, c):
    return a + b + c

r = addition(2, 3)  # Error
r = addition(1, 2, 3)  # 6
