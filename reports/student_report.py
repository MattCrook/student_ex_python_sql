import sqlite3
from nss_classes.student import Student


class StudentExerciseReports:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):
        """Retrieve all students with the cohort name"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Student(
                row[1], row[2], row[3], row[5])
            # conn.row_factory = lambda cursor, row: Student(*row)

            db_cursor = conn.cursor()

        # acts like a try/except/finally..Is like try to connect to this db with this path. If it can't it doesn't make the connection.
        # conn is a connection object
        # This line creates a new connection to the database
            execute_query = db_cursor.execute("""
            SELECT s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.Name
            FROM Students s
            JOIN Cohorts c ON s.cohort_id = c.Id
            ORDER BY s.cohort_id
            """)

            print("[EXECUTE QUERY]", execute_query)

            # This returns a query object. Not iterable. So we need to do fetchall. Which returns a [list] of (tuples). Each row is a tuple, bc we want it to be immutable. Ordered in same order that you listed.
            all_students = db_cursor.fetchall()

            # When there is no row_factory function defined, we get a list of tuples
            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # for student in all_students:
            #     new_student = Student(student[1], student[2], student[3], student[5])
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

        # for student in all_students:
        #     print(f'{student.first_name} {student.last_name} is in {student.cohort}')

        # for student in all_students:
        #     print(student)
        print("\n ****** Total Student Report *****\n")
        [print(s) for s in all_students]


print("\n [MRO]", Student.__mro__)
