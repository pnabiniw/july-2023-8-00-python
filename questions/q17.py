"""
Explain the concept of shallow copy and deepcopy

"""

a = [[1, 2, 3], 4]
b = a.copy()
print(a)  # [[1, 2, 3], 4]
print(b)  # [[1, 2, 3], 4]

a[0][1] = 7
print(a)   # [[1, 7, 3], 4]
print(b)   # [[1, 7, 3], 4]

from copy import deepcopy
b = deepcopy(a)
print(a)  # [[1, 7, 3], 4]
a[0][1] = 10
print(a)  # [[1, 10, 3], 4]
print(b)  # [[1, 7, 3], 4]
