##### Accessing characters in String ####
# We access characters from string using indexing. Indexing in string is similar to that of list
# Forward indexing starts from 0 and reverse indexing starts from -1

message = "Hello World"
print(message[0])  # H
print(message[3])  # l
print(message[5])  # <space>

print(message[-1])  # d
print(message[-3])  # r

# If we try to access index not present in the string then it raises error
# print(message[15])  # It raises index error
# print(message[-13])  # It raises index error


####### String Slicing ###########
# String slicing is also similar to list slicing
message = "Hello World"
print(message[0:3])  # Hel
print(message[:3])  # Hel
print(message[4:])  # o World
print(message[3:-2])  # lo Wor
print(message[2:5])  # llo
print(message[5:2])  # ""

print(message[0:-2])  # Hello Wor
print(message[:-2])  # Hello Wor
print(message[-4:])  # orld

print(message[-6: -2])  # " Wor"
print(message[-2: -6])  # ""


# Updating and Deleting string item
m = "Hello World"
# m[2] = "L"  # It raises error because string is immutable and item assignment is not possible

# del m[6]   # This is also npt possible
# But we can entirely delete the string object
del m  # It deletes the string object m


# Iterating string using for loop
message = "Hello World"
for i in message:
    print(i)  # H, e, l, l, o, , W, o, r, l, d

for i in message[2:7]:
    print(i)   # l, l, o, , W
