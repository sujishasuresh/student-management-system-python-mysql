CREATE DATABASE student_management;

USE student_management;

CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) NOT NULL
);