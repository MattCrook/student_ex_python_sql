import sqlite3


class StudentsWithExercises:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def all_students_with_exercises(self):

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                s.id,
                s.first_name,
                s.last_name
            FROM Exercise e
            JOIN Student_Exercises se ON se.excercise_id = e.id
            JOIN Students s ON s.id = se.student_id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            print("\n********* All Students With Exercises *********")
            for student, exercises in students.items():
                exercise_set = set()
                print(f"\n{student} is working on:")
                for exercise in exercises:
                    exercise_set.add(exercise)
                for exercise in exercise_set:
                    print(f"\t* {exercise}")
