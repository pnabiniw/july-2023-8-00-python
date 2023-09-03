"""
1. What is the order of the arguments in functions and methods
a. Keyword Args / Default Args
b. Positional
c. **kwargs
d. *args

2. Explain *args and **kwargs
"""

def addition(*args, **kwargs):
    print(args)   # (1, 2, 3, 4, 5)
    print(kwargs)  # {"p": 10, "q": 20}
    return sum(args) + sum(kwargs.values())

r = addition(1, 2, 3, 4, 5, p=10, q=20)
print(r)
