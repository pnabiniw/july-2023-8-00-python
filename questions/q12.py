"""
How to create private, protected and public attributes of classes in Python?
"""

class Student:
    __grade = 10  # private attribute
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self.age = age   # public attribute

    def get_info(self):
        pass

s = Student("Jon", 23)


class Student2(Student):
    def get_info(self):
        pass
