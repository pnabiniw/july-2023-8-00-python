# In Python the errors can be broadly classified into two sections:
# 1. Syntactic Error
# 2. Non-Syntactic Error

# Syntactic Error
# This type of error occurs when you mess up with the grammar of the language
# For example: making typo in keywords, messing up with indentations, whitespaces at unwanted places etc

 # a = 1  # Syntax error because of a white space in the beginning
 # fo i in range(10):  # Syntax error because of the type in keyword
 #     pass
# a = 5
# if a:
# print("Hello World")   # Indentation Error


# Non-Syntactic Error
# These are all the errors except syntax error. They can further be classified in followings:
# 1. TypeError
# 2. ValueError
# 3. ZeroDivision Error
# 4. Attribute Error
# 5. KeyError
# 6. IndexError
# 7. NameError
# 8. ModuleNotFoundError

# TypeError
# It is raised when operations in different datatypes are performed which is not acceptable
# For example: 2 + "Hello". Int and String can't be operated with '+' operator
# 2 + "Hello"  raises TypeError


# Value Error
# It is raised if we try to convert a datatype to other datatype which is not possible
# For example int("Hello"). This raises Value Error


# ZeroDivision Error
# It is raised when we try to divide an object with 0
# print(3 / 0)  # ZeroDivision Error


# Attribute Error
# It is raised if an object tries to get an attribute which is not present in that object
# example: if a list object tries to access the join() method. join() is actually a method in string.
# a = [1, 2, 3]
# a.join(" ")  # Attribute Error


# KeyError
# student = {"name": "Jon", "address": "KTM"}
# print(student["phone"])  # KeyError because phone is not present in the dictionary


# IndexError
# data = [1, 2, 3, 4]
# print(data[10])   # IndexError


# NameError
# a = 1
# print(b)  # NameError: 'b' is not defined


# ModuleNotFound Error
# import mat  # ModuleNotFoundError because "mat" is not a valid package
