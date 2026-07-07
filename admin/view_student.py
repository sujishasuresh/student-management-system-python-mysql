from database import conn,curr


def admin_view():
    query='SELECT * FROM STUDENT'
    curr.execute(query)
    students=curr.fetchall()

    if not students:
        print("No student records found.")
        return

    print("\n----- Student Details -----")

    for student in students:
        print(f"ID      : {student['student_id']}")
        print(f"Name    : {student['student_name']}")
        print(f"Gender  : {student['gender']}")
        print(f"DOB     : {student['dob']}")
        print(f"Email   : {student['email']}")
        print("-" * 30)
