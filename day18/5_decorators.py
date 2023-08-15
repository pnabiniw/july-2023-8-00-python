# decorators are the higher order function in python which adds extra functionality to the
# existing function

# If a function takes another function as an argument, then such a function is called higher
# order function. map(), reduce(), filter(), sorted(), all the decorators are higher order function


################ Closure ########################
# Closure is a concept in python which satisfies the following points
# 1. There should be a nested function i.e a function inside another function
# 2. Inner function must refer to the value of outer function
# 3. Outer function must return inner function

def outer_func(message):
    def inner_func():
        return message
    return inner_func


result = outer_func("Hello World")
print(result())
