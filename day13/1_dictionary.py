# Dictionary is the mutable datatype in python
# They have the elements in key-value pair format
# It is also the sequential datatype like list and tuple

# Creating an empty dictionary
a = dict()   # Empty dictionary
a = {}   # This is also an empty dictionary


# Creating a non-empty dictionary
student = {"name": "Jon", "age": 25, "department": "CS"}
print(student)  # {"name": "Jon", "age": 25, "department": "CS"}
student = dict(name="Jon", age=25, department="CS")
print(student)

student = dict({"name": "Jon", "age": 25, "department": "CS"})
print(student)

student = dict([("name", "Jon"), ("age", 25), ("department", "CS")])
print(student)  # {"name": "Jon", "age": 25, "department": "CS"}


# Creating a list of dictionaries
students = [
    {"name": "Jon", "age": 25, "department": "CS"},
    {"name": "Jane", "age": 32, "department": "IT"},
    {"name": "Hary", "age": 21, "department": "Physics"},
]
print(students)
