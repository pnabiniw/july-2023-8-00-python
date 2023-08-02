# We can loop through the list in following way

a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

b = []
for i in a:
    value = i ** 2
    b.append(value)
print(b)

# Recreating the above code using List Comprehension
result = [i**2 for i in a]
print(result)
