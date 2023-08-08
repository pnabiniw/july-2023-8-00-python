a = 2
b = 4
print(a)   # 2
print(b)   # 4

# Creating a temporary variable 'temp'
temp = a
a = b
b = temp
print(a)  # 4
print(b)  # 2


a = 1
b = 2
a, b = b, a
print(a)  # 2
print(b)  # 1
