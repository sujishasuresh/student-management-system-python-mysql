import pymysql
from database import curr,conn
from validation import (
    get_student_name,
    get_gender,
    get_dob,
    get_email,
)


def insert_student_details():
    print("Please enter below details!")
    # id=get_student_id()
    name=get_student_name()
    gender=get_gender()
    dob=get_dob()
    email=get_email()
    try:
        query="insert into student (student_name,gender,dob,email) values (%s,%s,%s,%s)"
        curr.execute(query,(name,gender,dob,email))
        conn.commit()
        id=curr.lastrowid
        print(f"Student '{name}' with ID {id} has been added successfully.")
    except pymysql.MySQLError as e:
        print("Database Error: ",e)
    

# insert_student_details()