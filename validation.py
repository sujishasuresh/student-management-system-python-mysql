from database import conn,curr
import pymysql
from database import curr,conn
import datetime
import re


def get_student_name():
    while True:
        valid=True
        name=input("Student name: ").strip()
        for part in name.split():
            if not part.isalpha():
                valid=False
                break
        if valid:   #if valid==True
            return name.title()
        else:
            print("Enter a valid student name")
            continue

def get_gender():
    while True:
        gender=input("Gender (Male/Female/Other): ").strip().lower()
        if gender in ('male','female','other'):
            return gender.capitalize()
        print("Enter valid gender")
        continue

def get_dob():
    while True:
        user_input=input("Dob(YYYY-MM-DD): ")
        try:
            dob=datetime.datetime.strptime(user_input,"%Y-%m-%d").date()
            return dob
        except ValueError:
            print("Input does not match the YYYY-MM-DD format, or the date is invalid.")
            continue

def get_email():
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email=input("Email: ")
        if re.fullmatch(email_pattern,email):
            return email
        else:
            print("Invalid email")
            continue

def validate_student_id():
    while True:
        try:
            student_id=int(input("Student ID: "))
            if student_id<=0:
                print("Student id must be greater than zero")
                continue
            query="select * from student where student_id = %s"
            curr.execute(query,(student_id,))
            if curr.fetchone():
                return student_id
            else:
                print("No student found with this ID.")
            
        except ValueError:
            print("Invalid student id type")
            continue

def validate_admin_username():
    pass

def validate_password():
    pass
