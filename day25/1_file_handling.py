# We can handle the files using Python
# In file handling we study how to open a file, read a file, write in a file and close a file

# r => Read Mode
# w => Write Mode
# r+ => Read and Write Mode
# w+ => Write and Read Mode

filename = "message.txt"
# fp = open(filename, "w")
# fp.write("Hello World")
# fp.close()

# fp = open(filename, "r")
# data = fp.read()
# fp.close()
# print(data)

fp = open(filename, "r+")
data = fp.read()
print(data)
fp.write(".I'm learning Python")
fp.close()


fp = open(filename, "w+")
fp.write("Python is a high level language")
data = fp.read()
fp.close()
print(data)
