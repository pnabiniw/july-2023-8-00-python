import json
filename = "students.json"


def update_student(student_id):
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())  # [{}, {}, {"id": 1, "name": "Jon", "address": "KTM"}]
        student = list(filter(lambda x: x['id'] == student_id, students))
        if student:
            student = student[0]  # {"id": 1, "name": "Jon", "address": "KTM"}
            key = input("Enter the info you want to update ")  # name
            if key.lower() not in ["name", "age", "address"]:
                print("Invalid User Info")
            else:
                value = input("Enter the new value ")  # Jane
                student[key] = value
                fp.seek(0)
                fp.write(json.dumps(students, indent=2))
                print("Student Updated Successfully !!")
        else:
            print("Please enter a valid student ID")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False
