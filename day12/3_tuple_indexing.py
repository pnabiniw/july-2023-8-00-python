# Indexing
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # "a"
# print(vowels[10])  # It raises error
print(vowels[2])  # "i"

print(vowels[-1])  # "u"
# print(vowels[-10])  # It raises error


# Slicing
# Tuple slicing is also similar to that of list
data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

print(data[:9])  # ("a", "b", "c", "d", "e", "f", "g", "h", "i")
print(data[0: 9])  # ("a", "b", "c", "d", "e", "f", "g", "h", "i")

print(data[4:])  # ("e", "f", "g", "h", "i", "j")
print(data[4: 9])  # ("e", "f", "g", "h", "i")
print(data[7: 3])  # ()

print(data[2: 9: 2])  # ("c", "e", "g", "i")  # Here last value in slicing is a step size

print(data[-8:])  # ("c", "d", "e", "f", "g", "h", "i", "j")
print(data[-7: -2])  # ("d", "e", "f", "g", "h")
print(data[:-4])  # ("a", "b", "c", "d", "e", "f")

print(data[-9: -1: 2])  # ("b", "d", "f", "h")


del data  # it deletes the tuple data
