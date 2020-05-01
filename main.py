from reports import StudentExerciseReports
from reports import ExerciseReport
from reports import InstructorReports
from reports import CohortReport
from reports import ExerciseJoinStudentReport



C_reports = CohortReport()
C_reports.all_cohorts()

E_reports = ExerciseReport()
E_reports.all_exercises()

I_reports = InstructorReports()
I_reports.all_instructors()

S_reports = StudentExerciseReports()
S_reports.all_students()

student_exercise_join_reports = ExerciseJoinStudentReport()
student_exercise_join_reports.all_students_all_exercises()

# OUTPUT
'''
 [MRO] (<class 'nss_classes.student.Student'>, <class 'nss_classes.nss.NSS'>, <class 'object'>)
[EXECUTE QUERY] <sqlite3.Cursor object at 0x1049f6c70>

 ****** All Cohorts *****

Cohort 37
Cohort 39
Cohort 38

 ****** Exercise Report *****

Student Exercises using the language: Python
Sockets using the language: HTML
JS Interpreter using the language: Calendar App
React Context using the language: JavaScript
Music History using the language: SQL

 ****** Instructor Report *****

Jisie David has the specialty of Teaching Back-End and teaches Cohort 37.
Kristen Norris has the specialty of Helping Students and teaches Cohort 39.
Andy Collins has the specialty of Taught Front End and teaches Cohort 38.

 ****** Total Student Report *****

Matt Crook is in Cohort 37
Keith Potempa is in Cohort 37
Matthew Kroeger is in Cohort 39
Sofia Candiani is in Cohort 39
Alyssa Nycum is in Cohort 38
Andrew Green is in Cohort 38
Dustin Murdock is in Cohort 38

 ************** Students and Exercises Final Report **********

[EXERCISE NAME]:  Student Exercises
        * Matt Crook
        * Alyssa Nycum
        * Andrew Green
[EXERCISE NAME]:  Sockets
        * Matt Crook
        * Sofia Candiani
        * Alyssa Nycum
[EXERCISE NAME]:  React Context
        * Dustin Murdock
        * Keith Potempa
        * Matthew Kroeger
[EXERCISE NAME]:  JS Interpreter
        * Dustin Murdock
        * Sofia Candiani
        * Matthew Kroeger
[EXERCISE NAME]:  Music History
        * Keith Potempa
        * Andrew Green

'''