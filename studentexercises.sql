-- Create Cohort TABLE
CREATE TABLE Cohorts
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);


-- Create Student TABLE
CREATE TABLE Students
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slack_handle TEXT NOT NULL UNIQUE,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY (cohort_id)
		REFERENCES Cohorts(id)
);

-- Create Instructor TABLE
CREATE TABLE Instructors (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL UNIQUE,
	last_name TEXT NOT NULL UNIQUE,
	slack_handle TEXT NOT NULL UNIQUE,
	specialty TEXT NOT NULL,
	cohort_id INTEGER NOT NULL,
	FOREIGN KEY (cohort_id)
		REFERENCES Cohorts(id)
);


-- Create Exercise TABLE
CREATE TABLE Exercise (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	language TEXT NOT NULL,
	name TEXT NOT NULL
);


-- Create Student_Exercises Table
CREATE TABLE Student_Exercises (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	student_id Integer NOT NULL,
	excercise_id Integer NOT NULL,
FOREIGN KEY (student_id) 
     REFERENCES Students(id),
FOREIGN KEY (excercise_id) 
     REFERENCES Exercise(id),
);

-- Use the INSERT INTO SQL statement to create...

-- 3 cohorts
Insert INTO Cohorts
    (name)
VALUES
    ("Cohort 38");

Insert INTO Cohorts
    (name)
VALUES
    ("Cohort 39");

Insert INTO Cohorts
    (name)
VALUES
    ("Cohort 37");


-- 5 exercises
INSERT INTO Exercise
    (language, name)
Values
    ("Python", "Student Exercises"),
    ("HTML", "Sockets"),
    ("Calendar App", "JS Interpreter"),
    ("JavaScript", "React Context"),
    ("SQL", "Music History")

-- 3 instructors
INSERT INTO Instructors
    (first_name, last_name, slack_handle, specialty, cohort_id)
VALUES
    ("Jisie", "David", "jisie", "Teaching Back-End", 1),
    ("Kristen", "Norris", "kristen.norris", "Helping Students", 2),
    ("Andy", "Collins", "dudewithglasses", "Taught Front End", 3)


-- 7 students (don't put all students in the same cohort)
INSERT INTO Students
    (first_name, last_name, slack_handle, cohort_id)
VALUES
    ("Matt", "Crook", "Matt", 1),
    ("Matthew", "Kroeger", "MatK", 2),
    ("Alyssa", "Nycum", "Alyssa Nycum", 3),
    ("Keith", "Potempa", "Kieth", 1),
    ("Sofia", "Candiani", "SofiaC", 2),
    ("Andrew", "Green", "AG", 3),
    ("Dustin", "Murdock", "Dusty", 3)


-- Assign 2 exercises to each student
INSERT INTO Student_Exercises
    (student_id, excercise_id, instructor_id)
VALUES
    (1, 1, 1),
    (1, 2, 3),
    (2, 4, 1),
    (2, 3, 2),
    (3, 2, 3),
    (3, 1, 1),
    (4, 5, 2),
    (4, 4, 3),
    (5, 3, 1),
    (5, 2, 3),
    (6, 1, 3),
    (6, 5, 2),
    (7, 4, 1),
    (7, 3, 2)

ALTER TABLE Student_Exercises
ADD instructor_id Integer NOT NULL,
FOREIGN KEY (instructor_id)
        REFERENCES Instructors(id);

INSERT INTO Student_Exercises
    (instructor_id)
VALUES(1),
    (2),
    (3),
    (1),
    (2),
    (1),
    (2),
    (3),
    (2),
    (1),
    (1),
    (2),
    (3),
    (1)


DELETE FROM Student_Exercises
CREATE TABLE Student_Exercises (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	student_id INTEGER NOT NULL,
	excercise_id INTEGER NOT NULL,
	instructor_id INTEGER NOT NULL
FOREIGN KEY
(student_id) 
    REFERENCES Students(id),
FOREIGN KEY
(excercise_id) 
    REFERENCES Exercise(id),
FOREIGN KEY
(instructor_id)
    REFERENCES Instructors(id)
);
