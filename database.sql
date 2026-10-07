CREATE DATABASE online_examination_system;

USE online_examination_system;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(100) NOT NULL,
    register_number VARCHAR(50) NOT NULL UNIQUE,
    marks INT DEFAULT 0,
    password VARCHAR(100) NOT NULL
);

INSERT INTO students
(student_id, name, age, department, register_number, marks, password)
VALUES
('STU001', 'DivyaDharshiniD', 20, 'B.Tech', '711525BAD047', 85, '12345');

INSERT INTO students
(student_id, name, age, department, register_number, marks, password)
VALUES
('STU002', 'student2', 20, 'B.Tech', '711525BAD048', 78, '12345');

SELECT * FROM students;