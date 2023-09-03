from estd_connection import estd_connection


def create_student():
    cursor = estd_connection()
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age ")
    address = input("Enter student address ")
    sql = f"""
    INSERT INTO STUDENTINFO (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', {age}, '{address}')
    """
    cursor.execute(sql)
    print("Student Added Successfully !!")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False

