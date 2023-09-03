# Calculate the factorial of 5 using normal loop, reduce() function and recursive function

# 5*4*3*2*1

fact = 1
for i in range(1, 6):
    fact = fact * i
print("Factorial is", fact)


# reduce()
from functools import reduce

result = reduce(lambda x, y: x*y, range(1, 6))
print(result)


# Recursive function
# If a function call is made from inside the definition of the same function then such a function is called
# a recursive function

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# 5 * factorial(4)  # 5 * 24 = 120
# 4 * factorial(3)  # 4 * 6 = 24
# 3 * factorial(2)   # 3 * 2 = 6
# 2 * factorial(1)   # 2 * 1 = 2
# 1 * factorial(0) => 1 * 1 = 1

result = factorial(5)
print(result)  # 120

