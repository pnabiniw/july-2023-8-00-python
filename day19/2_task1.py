# Create a decorator to change all the characters of the input function to upper case

def to_upper_case(func):
    def inner_func(info):
        return func(info).upper()
    return inner_func


@to_upper_case
def message(info):
    return info


result = message("Hello Im learning Python")
print(result)
