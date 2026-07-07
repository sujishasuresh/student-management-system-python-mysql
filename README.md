# Student Management System

## About the Project

The **Student Management System** is a console-based application developed using **Python** and **MySQL**. It demonstrates fundamental database operations, modular programming, and Python-MySQL integration. The project is designed with separate modules for administrators and students, making the code organized, maintainable, and easy to extend.

---

## Features

### Admin Module

* Secure administrator login
* Add new student records
* Delete student records
* View all student records

### Student Module

* View personal student details using Student ID

---

## Technologies Used

* **Programming Language:** Python
* **Database:** MySQL
* **Database Connector:** PyMySQL
* **Version Control:** Git & GitHub
* **IDE:** Visual Studio Code

---

## Project Structure

```text
student-management-system/
│
├── admin/
│   ├── add_student.py
│   ├── delete_student.py
│   ├── view_student.py
│   └── admin_login.py
│
├── student/
│   ├── student_login.py
│   └── student_view.py
│
├── database.py
├── validation.py
├── main.py
├── requirements.txt
├── schema.sql
├── .gitignore
└── README.md
```

---

## Sample Output

### Main Menu

```text
===== Student Management System =====
1. Admin Login
2. Student Login
3. Exit
```

### Admin Menu

```text
==== Admin Menu ====
1. Add Student Details
2. Delete Student Details
3. View Student Details
```

### Student Module

```text
---- Student Details ----
Student ID : 1
Name       : Taylor
Gender     : Female
DOB        : 2000-01-15
Email      : taylor20@gmail.com
```

---

## Future Enhancements

* Update student records
* Student authentication using passwords
* Search students by ID or name
* Enhanced console-based user interface
* Graphical User Interface (GUI)
* Role-based authentication with multiple user levels


