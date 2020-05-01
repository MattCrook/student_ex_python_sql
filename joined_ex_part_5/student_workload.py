import sqlite3


class StudentAssignedWorkloadByInstructor:
    def __init__(self):
        self.db_path = "/Users/matthewcrook/code/nss/backEnd/Book2/student_exercises/studentexercises.db"

    def student_assigned_workload(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_curser = conn.cursor()

            db_curser.execute('''
            SELECT
                i.first_name,
                i.last_name,
                e.name
            FROM Student_Exercises se
            JOIN Instructors i ON i.id = se.instructor_id
            JOIN Exercise e ON e.id = se.excercise_id
            ''')

            dataset = db_curser.fetchall()

            for row in dataset:
                first = row[0]
                last = row[1]
                exercise = row[2]
                full_name = f'{row[0]} {row[1]}'

            # for first, last, exercise in dataset:
            #     if f"{first} {last}" not in {instructors}:
            #         instructors[f"{first} {last}"] = [exercise]

                if full_name not in instructors:
                    instructors[f"{first} {last}"] = [exercise]
                else:
                    if exercise not in instructors[f"{first} {last}"]:
                        instructors[f"{first} {last}"].append(exercise)

            print("********** Exercises Instructors Assigned **********")
            for instructor, exercises in instructors.items():
                print(f"\n{instructor} has assigned the exercise:")
                for exercise in exercises:
                    print(f"\t* {exercise}")
