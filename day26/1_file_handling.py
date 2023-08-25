# Different modes in which files can be opened
# r => read mode
# w => write mode
# a => append mode
# r+ => read and write mode
# w+ => write and read mode
# a+ => append and read mode
# x => write exclusively mode

filename = "message.txt"
fp = open(filename, "w")
fp.write("Hello World")
fp.close()


fp = open(filename, "r")
data = fp.read()
print(data)
fp.close()


# fp = open(filename, "a")
# fp.write("\nI'm Learning Python")
# fp.close()


# file handling with context manager
with open(filename, "r") as fp:
    data = fp.read()
print(data)


# with open(filename, "r+") as fp:
#     data = fp.read()  # first read
#     fp.write("Python is a high level language")  # and then write
# print(data)


with open(filename, "w+") as fp:
    fp.write("I'm learning Python")
    data = fp.read()
print(data)


# exclusive mode doesn't create a file if the file already exists. It raises error
# in such a case
# with open(filename, "x") as fp:
#     fp.write("Hello World")
