squared = {data: data**2 for data in range(1, 13)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16}

student_list = [("name", "Jon"), ("age", 25), ("address", "KTM")]
student = dict(student_list)
print(student)

# Create dictionary of the above data using dictionary comprehension
student = {key: value for key, value in student_list}
print(student)
