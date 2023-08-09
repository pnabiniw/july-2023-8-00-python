# Membership operation
# Membership is checked only in dictionary keys but not in values
student = {"name": "Jon", "age": 25, "department": "CS"}
print("name" in student)  # True
print("Jon" in student)  # False


# Built-in functions
print(len(student))  # 3

result = sorted(student)
print(result)  # ["age", "department", "name"]

print(str(student))  # "{"name": "Jon", "age": 25, "department": "CS"}"
