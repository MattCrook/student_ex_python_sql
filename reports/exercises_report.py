import sqlite3
from nss_classes.exercise import Exercise


class ExerciseReport:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Exercise(
                row[1], row[2])

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT * FROM Exercise
            ORDER By Exercise.id
            """)

            exercises = db_cursor.fetchall()

        print("\n ****** Exercise Report *****\n")
        [print(s) for s in exercises]
