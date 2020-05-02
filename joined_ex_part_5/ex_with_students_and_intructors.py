import sqlite3


class ExercisesWithStudentsAndInstructors:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def who_working_on_what(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.name,
                i.first_name,
                i.last_name,
                s.first_name,
                s.last_name
            FROM Student_Exercises es
            JOIN Exercise e ON
                e.id = es.excercise_id
            JOIN Instructors i ON
                i.id = es.instructor_id
            JOIN Students s ON
                s.id = es.student_id
            """)

            data = db_cursor.fetchall()

            print("\n******* Who is Working on What and Why? *******")
            for exercise, i_first, i_last, s_first, s_last in data:
                if exercise not in exercises:
                    exercises[exercise] = [{
                        "student": f"{s_first} {s_last}", "instructor": f"{i_first} {i_last}"}]
                else:
                    exercises[exercise].append({
                        "student": f"{s_first} {s_last}", "instructor": f"{i_first} {i_last}"})

            for exercise, info in exercises.items():
                print(f"\n{exercise}:")
                for item in info:
                    print(f"  * {item['instructor']} assigned this to {item['student']}")

    def ex_with_st_and_instr(self):
        cohorts = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                c.name,
                s.first_name,
                s.last_name
            FROM Cohorts c
            LEFT JOIN Students s ON
                s.cohort_id = c.id
            """)

            student_data = db_cursor.fetchall()

            for c_name, first, last in student_data:
                if c_name not in cohorts:
                    cohorts[c_name] = {"students": [
                        f"{first} {last}"], "instructors": []}
                else:
                    cohorts[c_name]["students"].append(f"{first} {last}")

            db_cursor.execute("""
            SELECT
                c.name,
                i.first_name,
                i.last_name
            FROM Cohorts c
            LEFT JOIN Instructors i ON
                i.cohort_id = c.id
            """)

            instructor_data = db_cursor.fetchall()
            for c_name, first, last in instructor_data:
                if c_name not in cohorts:
                    cohorts[c_name] = {"instructors": [
                        f"{first} {last}"], "students": []}
                else:
                    cohorts[c_name]["instructors"].append(f"{first} {last}")

            print("\n***** Instructors and Students *****")

            for cohort, people in cohorts.items():
                print(f"\n{cohort}")
                print("  Students:")
                for student in people["students"]:
                    print(f"  * {student} is in {cohort}")
                print("  Instructors:")
                for instructor in people["instructors"]:
                    print(f"  * {instructor} is in {cohort}")
