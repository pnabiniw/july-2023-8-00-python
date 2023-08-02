# We can concatenate strings

m1 = "Hello"
m2 = "World"
message = m1 + m2
print(message)  #

# Repetition operation / Broadcast Operation

message = "Hello World"
print(message * 3)  # "Hello WorldHello WorldHello World


# Membership Operation
message = "Hello World"
print("H" in message)  # True
print("W" not in message)  # False
print("K" in message)  # False



##### Built-in functions that can be used in string #####

message = "Hello World"
print(len(message))  # 11
print(bool(message))  # True
print(type(message))  # <class 'str'>

x = slice(2, 6)
print(message[x])  # "llo "
