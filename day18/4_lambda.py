# lambda in python are the elegant way to create a one-liner functions
# These functions do not have name. So, they are also called as anonymous function


def addition(a, b):
    return a + b


summ = lambda a, b: a + b
print(summ(4, 5))

is_even = lambda x: x % 2 == 0
print(is_even(4))
