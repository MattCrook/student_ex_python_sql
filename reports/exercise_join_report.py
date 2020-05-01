import sqlite3


class ExerciseJoinStudentReport:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def all_students_all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            exercises = dict()

            db_cursor.execute("""
                SELECT
                    Exercise.id,
                    Exercise.name,
                    Students.id,
                    Students.first_name,
                    Students.last_name
                FROM Exercise
                JOIN Student_Exercises se ON se.excercise_id = Exercise.id
                JOIN Students ON Students.id = se.student_id
            """)

            dataset = db_cursor.fetchall()

            print("\n ************** Students and Exercises Final Report **********\n")

            for row in dataset:
                # print(row)
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                # print(f"[EXERCISES DICT]: ", exercises)

            for exercise_name, students in exercises.items():
                print(f"[EXERCISE NAME]: ", exercise_name)
                student_set = set()
                for student in students:
                    student_set.add(student)
                # print(f'\t* {student_set}')

                for student in student_set:
                    print(f'\t* {student}')

# Had to turn into set from the dict values because kept getting duplicate student names. Looked like initial loop
# to go thru all exercises loops (3) times, so there was three entries of each student. 
