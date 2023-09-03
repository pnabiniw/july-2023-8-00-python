from estd_connection import estd_connection


def update_student(student_id):
    cursor = estd_connection()
    to_change = input("Enter the data you want to change ")
    changed_value = input(f"Enter new {to_change} ")

    sql = f"""
    UPDATE STUDENTINFO SET {to_change}='{changed_value}' WHERE ID='{student_id}'
    """

    cursor.execute(sql)
    print("Your Record Has Been Updated !!")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False
