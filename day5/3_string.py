# Strings are immutable and sequence data-type in python
# Creating an empty string
a = ""  # empty string
b = ''  # empty string
c = """"""  # empty string
d = str()  # empty string

# Creating a non-empty string
a = "Hello World"
b = 'Python is a high level language'
c = """
Hello World.
Python is awesome.
"""


# Quote characters
a = "I'm learning python"
b = 'He said, "Python is easy to learn"'

# We can also use escape characters for in strings with quote
a = 'I\'m learning Python'
b = "He said, \"Python is easy to learn\""


# Escape characters are the characters in python which suppress the actual python
# meaning and gives new meaning to that character.
# \', \", \n, \t etc are the examples of escape characters

print("Hello\nWorld")  # Prints Hello in first line and World in second line
print("Hello\tWorld")  # Prints Hello, a tab, and World


# Python also has Triple quoted strings
message = """
I'm learning python
"""
message = '''
I'm learning python
'''
# There is no need for \' (escape sequence) for triple quoted strings
# Triple quoted strings are not only used as normal strings, but are also used to
# add code descriptions in functions, classes and as multiline comments


def addition(a, b):
    """

    :param a: any integer value
    :param b: any integer value
    :return: sum of a and b
    """
    return a + b
