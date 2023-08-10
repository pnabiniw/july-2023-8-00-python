# copy()
student = {"name": "Jon", "age": 25}
student2 = student.copy()
print(student2)  # {"name": "Jon", "age": 25}
print(student)  # {"name": "Jon", "age": 25}

# get()
student = {"name": "Jon", "age": 25}
name = student.get("name")
print(name)
roll = student.get("roll")
print(roll)  # None
roll = student.get("roll", 1)
print(roll)  # 1
name = student.get("name", "Ram")
print(name)  # Jon


# items()
student = {"name": "Jon", "age": 25, "roll": 22}
print(student.items())

# keys()
student = {"name": "Jon", "age": 25, "roll": 22}
print(student.keys())

# values()
student = {"name": "Jon", "age": 25, "roll": 22}
print(student.values())


# pop()
student = {"name": "Jon", "age": 25, "roll": 22}
age = student.pop("age")
print(age)  # 25
print(student)  # {"name": "Jon", "roll": 22}


# popitem()
student = {"name": "Jon", "age": 25, "roll": 22}
result = student.popitem()
print(result)  # ("roll", 22)
print(student)  # {"name": "Jon", "age": 25}

# update()
student = {"name": "Jon", "age": 25, "roll": 22}
student.update(address="KTM")
print(student)  # {"name": "Jon", "age": 25, "roll": 22, address: "KTM}


# fromkeys()
a = dict()
result = a.fromkeys([1, 2], "a")
print(a)  # {1: "a", 2: "a"}
print(result)


# setdefault()
student = {"name": "Jon", "age": 25, "roll": 22}
student.setdefault("name", "Jane")
print(student)

student.setdefault("address", "KTM")
print(student)  # {"name": "Jon", "age": 25, "roll": 22, "address": "KTM"}

