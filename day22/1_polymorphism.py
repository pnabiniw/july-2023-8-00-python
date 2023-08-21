# Polymorphism means many forms of same the same function or object
# We can take the example of len, sum, min, max etc. built-in functions to observe polymorphism in
# python

# len() is a built-in function in python which can take any type of iterable as a parameter and gives
# the length of the iterable

print(len([1, 2, 3]))  # 3 (list)
print(len((1, 2, 3)))  # 3 (tuple)
print(len({"name": "Jane", "address": "KTM"}))  # 2 (dict)

# regardless of the datatype, len returns the length of an iterable


# We can classify polymorphism to three different variations in Python
# 1. Function / Method Overloading
# 2. Method Overriding
# 3. Operator Overloading

