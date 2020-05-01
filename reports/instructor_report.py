import sqlite3
from nss_classes.instructor import Instructor


class InstructorReports:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def all_instructors(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Instructor(
                row[1], row[2], row[3], row[4], row[5])

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute('''
            SELECT i.id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.specialty,
                c.Name
            FROM Instructors i
            JOIN Cohorts c ON i.cohort_id = c.Id
            ORDER BY i.cohort_id
            ''')

            all_instructors = db_cursor.fetchall()

        print("\n ****** Instructor Report *****\n")
        [print(i) for i in all_instructors]
