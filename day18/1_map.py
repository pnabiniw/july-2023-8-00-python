# map()
# map() is a built-in function that takes two parameters as an input. First parameter is a function
# and second parameter is an iterable.
# map() function changes every element in an iterable to some other form

nums = [1, 2, 3, 4, 5]


def increase_by_10(data):
    return data + 10


result = map(increase_by_10, nums)
print(nums)
print(list(result))

result = map(lambda x: x + 10, nums)
print(list(result))


nums = [1, 2, 3, 4, 5]
def get_cubed_data(data):
    return data ** 3

result = map(get_cubed_data, nums)
print(list(result))

nums = [1, 2, 3, 4, 5]
result = map(lambda x: x**3, nums)
print(list(result))





nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x**3, nums)
print(list(result))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
