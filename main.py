from admin.login import get_admin_credentials
from student.view_student import student_view



ADMIN='1'
STUDENT='2'
EXIT='3'

print("===== Student Management System =====") 
print("1.Admin Login")
print("2.Student Login")
print("3.Exit")
while True:
    user_Choice=input("Enter your choice: (1/2/3): ").strip()
    if user_Choice==ADMIN:
        get_admin_credentials()
        break
    elif user_Choice==STUDENT:
        student_view()
        break
    elif user_Choice==EXIT:
        print("Exit!")
        break
    else:
        print("Invalid choice")
        continue
