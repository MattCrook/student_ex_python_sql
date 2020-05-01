-- Create Cohort TABLE
CREATE TABLE Cohorts
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);
-- Create Student TABLE
CREATE TABLE Students (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL UNIQUE,
	last_name TEXT NOT NULL UNIQUE,
	slack_handle TEXT NOT NULL UNIQUE,
	cohort_id INTEGER NOT NULL,
	FOREIGN KEY (cohort_id) REFERENCES Cohorts (id)
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
        REFERENCES Exercise(id)
);
-- Use the INSERT INTO SQL statement to create...
-- 3 cohorts

INSERT INTO Cohorts (name)
		VALUES("Cohort 38");

INSERT INTO Cohorts (name)
		VALUES("Cohort 39");

INSERT INTO Cohorts (name)
        VALUES("Cohort 37");


-- 5 exercises
INSERT INTO Exercise
    (language, name)
VALUES
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
    (student_id, excercise_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 4),
    (2, 3),
    (3, 2),
    (3, 1),
    (4, 5),
    (4, 4),
    (5, 3),
    (5, 2),
    (6, 1),
    (6, 5),
    (7, 4),
    (7, 3)
