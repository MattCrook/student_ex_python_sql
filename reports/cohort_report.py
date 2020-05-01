import sqlite3
from nss_classes import Cohort

class CohortReport:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Cohort(
                row[1])
            # conn.row_factory = lambda cursor, row: Student(*row)

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT * FROM Cohorts
            ORDER BY Cohorts.id
            """ )
            print("[EXECUTE QUERY]", execute_query)

            all_cohorts = db_cursor.fetchall()

        print("\n ****** All Cohorts *****\n")
        [print(c) for c in all_cohorts]
