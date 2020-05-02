import sqlite3


class PopularExercises:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def popular_exercises(self):

        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    s.first_name,
                    s.last_name,
                    e.name
                FROM Student_Exercises se
                JOIN Students s ON
                    s.id = se.student_id
                JOIN Exercise e ON
                    e.id = se.excercise_id
                """)

            data = db_cursor.fetchall()
            print("\n******** Popular Exercises ********")

            ##### Can loop through the data (2) different ways:#######

            '''for first, last, exercise_name in data:
                if exercise_name not in exercises:
                    exercises[exercise_name] = [f"{first} {last}"]
                elif f"{first} {last}" not in exercises[exercise_name]:
                    exercises[exercise_name].append(f"{first} {last}")

            for name, students in exercises.items():
                print(f"\n{name} is being completed by:")
                for student in students:
                    print(f"\t* {student}")'''

            # This is slightly more explicit
            for row in data:
                first = row[0]
                last = row[1]
                exercise_name = row[2]

                if exercise_name not in exercises:
                    exercises[exercise_name] = [f"{first} {last}"]
                elif f"{first} {last}" not in exercises:
                    exercises[exercise_name].append(f"{first} {last}")

            for name, students in exercises.items():
                print(f"\n{name} is being completed by:")
                for student in students:
                    print(f"\t* {student}")
