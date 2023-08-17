class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"Name is {self.name} and age is {self.age}"


person = Person("Jon", 30)
print(person.description())
