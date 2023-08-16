def decorate_me(func):
    def inner_func(a, b):
        print("This is executed before the main function !")
        return func(a, b)
    return inner_func


@decorate_me
def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)
