student = {"id": 1, "name": "Jane", "age": 30, "address": "KTM"}
try:
    key = input("Enter the key you want to access ")
    data = student[key]
    print(f"The {key} of the student is {data}")
except KeyError:
    print("Please enter a valid key")
