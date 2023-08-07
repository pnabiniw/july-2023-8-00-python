# We can format string using f-strings
name = input("Enter your name ")
age = int(input("Enter your age "))
language = input("Enter the language you are learning ")
message = f"Hello I am {name}. I am learning {language}"
print(message)


message = 'I am %s and I am %d years old' % (name, age)
print(message)
message = f'I am {name} and I am {age} years old'
print(message)

#### Using format() method ####
message = "I am {} and I am {} years old."
formatted_message = message.format(name, age)
print(formatted_message)

message = 'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen', 'copy')
print(message)

# message = 'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen')  # It raises error

message = 'I have {} and {} in my bag.'.format('book', 'pen', 'copy', "pencil")
print(message)  # here first placeholder takes 'book', second placeholder takes 'pen' and other are ignored
