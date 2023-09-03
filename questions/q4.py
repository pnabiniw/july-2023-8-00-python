"""
1. What are the methods to get keys, values and key-value pair in dictionary?
2. How to loop in key-value pair?

"""

student = {"name": "Jon", "email": "j@j.com"}
student.keys()
student.values()
student.items()   # [("name", "Jon"), ("email", "j@j.com")]

for key, value in student.items():
    print(key)
    print(value)

key, value = "name", "Jon"
