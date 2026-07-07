from database import curr
from validation import validate_student_id



def student_view():
    retrieve_id=validate_student_id()
    query1="SELECT * FROM student WHERE student_id=%s"
    curr.execute(query1,(retrieve_id,))
    student=curr.fetchone()
    print("----Student Details----")
    print(f"Student id: {student['student_id']}")
    print(f"Student name: {student['student_name']}")
    print(f"Gender: {student['gender']}")
    print(f"DOB: {student['dob']}")
    print(f"Email: {student['email']}")


