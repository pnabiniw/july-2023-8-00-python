"""
What are magic methods? Explain with examples.
"""

a = 1
b = 2
print(a + b)
r = a.__add__(b)
print(r)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(5)
c2 = Circle(10)
if c1 > c2:
    print("c1 is larger")
else:
    print("c2 is larger")

