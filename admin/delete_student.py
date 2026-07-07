from database import conn,curr
import pymysql
from validation import validate_student_id



def remove_student_details():
    student_id=validate_student_id()
    while True:
        try:
            choice=input("Are you sure you want to delete this student? (Y/N): ").strip().lower()
            if choice in ('y','n'):
                if choice=="y":
                    query="DELETE FROM student WHERE student_id=%s"
                    curr.execute(query,(student_id,))
                    conn.commit()
                    print(f"Details of student with ID {student_id} has been deleted")
                    break
                else:
                    print("Deletion cancelled.")
                    break
            else:
                print("Please enter Y or N.")
                continue
        except pymysql.MySQLError as e:
            print("Database error",e)
        

