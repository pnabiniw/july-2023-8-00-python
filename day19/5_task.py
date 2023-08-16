s = "All the occurrences of a specified character in a given string"
char = input("Pick a character ")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each
print(result)

