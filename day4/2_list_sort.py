# sort() method is used to sort the elements of the list in ascending
# or descending order and alphabetically for strings

numbers = [7, 3, 4, 1, 8, 6, 2, 5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [(5, 4), (3, 2), (1, 9), (6, 1)]
# Expected Result [(6, 1), (3, 2), (5, 4), (1, 9)]
def sort_with_second_item(data):
    return data[1]


numbers.sort(key=sort_with_second_item)
print(numbers)


a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def sort_with_last_item(data):
    return data[-1]

a.sort(key=sort_with_last_item, reverse=True)
print(a)


fruits = ["banana", "apple", "mango"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
