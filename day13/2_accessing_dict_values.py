vowels = ["a", "e", "i", "o", "u"]
print(vowels[4])  # u


# Accessing dictionary is similar to that of accessing list elements
student = {"name": "Jon", "age": 25, "department": "CS"}
dept = student["department"]
print(dept)   # CS

name = student["name"]
print(name)  # Jon

# print(student["dob"])   # This raises KeyError

# accessing values using get() method
department = student.get("department")
print(department)  # CS
dob = student.get("dob")
print(dob)  # None


# Adding key-value pair in a dictionary
vowels = ["a", "e", "i", "o"]
vowels.append("u")
vowels.insert(2, "A")
vowels[1] = "E"

student = {"name": "Jon", "age": 25, "department": "CS"}
student["dob"] = "22 July"
print(student)  # {"name": "Jon", "age": 25, "department": "CS", "dob": "22 July"}

student.update(roll_no=12)
print(student)  # {"name": "Jon", "age": 25, "department": "CS", "dob": "22 July", "roll_no": 12}

student["name"] = "Jane"
print(student)  # {"name": "Jane", "age": 25, "department": "CS", "dob": "22 July", "roll_no": 12}


# Removing a key-value pair from a dictionary
student = {"name": "Jane", "age": 25, "department": "CS", "dob": "22 July", "roll_no": 12}
result = student.pop("dob")
print(result)  # 22 July
print(student)  # {"name": "Jane", "age": 25, "department": "CS", "roll_no": 12}

# result = student.pop("address")  # KeyError
# print(result)

result = student.popitem()
print(result)  # ("roll_no", 12)
print(student)  # {"name": "Jane", "age": 25, "department": "CS"}

student.clear()
print(student)  # {}

del student  # deletes the object
