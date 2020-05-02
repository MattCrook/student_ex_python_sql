from reports import StudentExerciseReports
from reports import ExerciseReport
from reports import InstructorReports
from reports import CohortReport
from reports import ExerciseJoinStudentReport
from joined_ex_part_5 import StudentsWithExercises
from joined_ex_part_5 import StudentAssignedWorkloadByInstructor
from joined_ex_part_5 import PopularExercises
from joined_ex_part_5 import ExercisesWithStudentsAndInstructors



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

student_with_exercises = StudentsWithExercises()
student_with_exercises.all_students_with_exercises()

student_assigned_workload_by_instructors = StudentAssignedWorkloadByInstructor()
student_assigned_workload_by_instructors.student_assigned_workload()

popular_exercises = PopularExercises()
popular_exercises.popular_exercises()

who_working_on_what = ExercisesWithStudentsAndInstructors()
who_working_on_what.who_working_on_what()
who_working_on_what.ex_with_st_and_instr()

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

********* All Students With Exercises *********

Matt Crook is working on:
        * Student Exercises
        * Sockets

Matthew Kroeger is working on:
        * JS Interpreter
        * React Context

Alyssa Nycum is working on:
        * Sockets
        * Student Exercises

Keith Potempa is working on:
        * Music History
        * React Context

Sofia Candiani is working on:
        * Sockets
        * JS Interpreter

Andrew Green is working on:
        * Music History
        * Student Exercises

Dustin Murdock is working on:
        * JS Interpreter
        * React Context

********** Exercises Instructors Assigned **********

Jisie David has assigned the exercise:
        * Student Exercises
        * React Context
        * JS Interpreter

Andy Collins has assigned the exercise:
        * Sockets
        * React Context
        * Student Exercises

Kristen Norris has assigned the exercise:
        * JS Interpreter
        * Music History


******** Popular Exercises ********

Student Exercises is being completed by:
        * Matt Crook
        * Alyssa Nycum
        * Andrew Green

Sockets is being completed by:
        * Matt Crook
        * Alyssa Nycum
        * Sofia Candiani

React Context is being completed by:
        * Matthew Kroeger
        * Keith Potempa
        * Dustin Murdock

JS Interpreter is being completed by:
        * Matthew Kroeger
        * Sofia Candiani
        * Dustin Murdock

Music History is being completed by:
        * Keith Potempa
        * Andrew Green

***** Instructors and Students *****

Cohort 37
  Students:
  * Keith Potempa is in Cohort 37
  * Matt Crook is in Cohort 37
  Instructors:
  * Jisie David is in Cohort 37

Cohort 39
  Students:
  * Matthew Kroeger is in Cohort 39
  * Sofia Candiani is in Cohort 39
  Instructors:
  * Kristen Norris is in Cohort 39

Cohort 38
  Students:
  * Alyssa Nycum is in Cohort 38
  * Andrew Green is in Cohort 38
  * Dustin Murdock is in Cohort 38
  Instructors:
  * Andy Collins is in Cohort 38


******* Who is Working on What and Why? *******

Student Exercises:
  * Jisie David assigned this to Matt Crook
  * Jisie David assigned this to Alyssa Nycum
  * Andy Collins assigned this to Andrew Green

Sockets:
  * Andy Collins assigned this to Matt Crook
  * Andy Collins assigned this to Alyssa Nycum
  * Andy Collins assigned this to Sofia Candiani

React Context:
  * Jisie David assigned this to Matthew Kroeger
  * Andy Collins assigned this to Keith Potempa
  * Jisie David assigned this to Dustin Murdock

JS Interpreter:
  * Kristen Norris assigned this to Matthew Kroeger
  * Jisie David assigned this to Sofia Candiani
  * Kristen Norris assigned this to Dustin Murdock

Music History:
  * Kristen Norris assigned this to Keith Potempa
  * Kristen Norris assigned this to Andrew Green
'''
