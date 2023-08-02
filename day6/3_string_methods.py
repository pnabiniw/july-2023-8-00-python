message = "hello world"

########### String Methods ##################
# capitalize()
result = message.capitalize()
print(result)

# title()
result = message.title()
print(result)

# upper()
result = message.upper()
print(result)

# lower()
result = message.lower()
print(result)


# split()
message = "hello world"
result = message.split()
print(result)  # ["hello", "world"]

result = message.split('o')
print(result)  # ["hell", " w", "rld"]

message = "I,am,learning,python"
result = message.split(",")
print(result)  # ["I", "am", "learning", "python"]


# join()
message = ["I", "am", "learning", "python"]
result = " ".join(message)
print(result)  # I am learning python

# message.join(" ")  # this raises error

# result => I, am, learning, python
result = ", ".join(message)
print(result)


# find()
message = "hello world"
result = message.find("l")
print(result)  # 2

result = message.find("wor")
print(result)  # 6

result = message.find("Wor")
print(result)  # -1


# replace()
message = "hello world"
result = message.replace("hello", "HELLO")
print(result)
