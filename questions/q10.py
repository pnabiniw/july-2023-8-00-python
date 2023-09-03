"""
What are class attributes and instance attributes? Give example

"""

class Student:
    grade = 10  # class attribute
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age   # instance attribute

s = Student("Jon", 23)

