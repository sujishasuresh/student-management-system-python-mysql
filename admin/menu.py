from admin.add_student import insert_student_details
from admin.delete_student import remove_student_details
from admin.view_student import admin_view

ADD_STUDENT='1'
DELETE_STUDENT='2'
VIEW_STUDENT='3'
# UPDATE_STUDENT='4'

def display_admin_menu():
    print("====Admin Menu====")
    while True:
        print("1. Add student details")
        print("2. Delete student details")
        print("3. View student details")
        # print("4. Update student details")
        choice=input("Enter your choice: ").strip().lower()

        if choice==ADD_STUDENT:
            print("Add student")
            insert_student_details()
        elif choice==DELETE_STUDENT:
            print("Remove student")
            remove_student_details()
        elif choice==VIEW_STUDENT:
            print("View student")
            admin_view()
        # elif choice==UPDATE_STUDENT:
        #     print("Update student")
        else:
            print("Invalid choice")
            continue
        should_continue=input("Do you want to continue? (Y?N): ").strip().lower()
        if should_continue=='y':
            continue
        elif should_continue=='n':
            print("Exit!")
            break
        else:
            print("Invalid input. Type 'Y' or 'N' to exit.")

