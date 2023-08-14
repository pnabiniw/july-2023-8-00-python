# Functions are the block of codes that are re-usable
# If the same lines of code are repeated at multiple places in the code, then we can define a function
# for that code block and call wherever necessary

# There are things we need to keep in mind while creating a function:
# 1. Function Definition
# 2. Function Call

# Let's create a simple function to check whether a number is odd or even

def is_even(number):  # This is a function definition
    if number % 2 == 0:
        return True
    else:
        return False


def is_even_n(number):
    return number % 2 == 0


result = is_even(43)   # Function call
print(result)


def addition(n1, n2):   # Function definition
    return n1 + n2


result = addition(4, 5)  # Function call
print(result)  # 9
