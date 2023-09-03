from estd_connection import estd_connection


def read_student(student_id):
    cursor = estd_connection()
    sql = f"""
    SELECT * FROM STUDENTINFO WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == "y" else False
