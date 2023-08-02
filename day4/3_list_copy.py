a = [1, 2, 3]
b = a
print(a)
print(b)
print(a is b)

b = a.copy()
print(b)
print(a is b)

# But there is a concept of shallow copy and deep copy
a = [[1, 2, 3], 4, 5]
b = a.copy()
print(a)
print(b)
# Both a and b have same value

a[2] = 6
print(a)  # [[1, 2, 3], 4, 6]
print(b)  # [[1, 2, 3], 4, 5]
# This proves that if immutable element of 'a' is changed then nothing changes in 'b'

a[0][1] = 7
print(a)  # [[1, 7, 3], 4, 6]
print(b)  # [[1, 7, 3], 4, 5]
# But if mutable element of one list is changed then the change is also reflected in its copy


# Python provides a function to entirely make a new copy of an object which is called deepcopy.
from copy import deepcopy
a = [[1, 2, 3], 4, 5]
b = deepcopy(a)
print(a)
print(b)

a[0][1] = 7
print(a)  # [[1, 7, 3], 4, 5]
print(b)  # [[1, 2, 3], 4, 5]
