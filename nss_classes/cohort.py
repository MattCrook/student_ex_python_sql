import json


class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def print_details(self):
        new_dict = self.__dict__
        new_list = list()
        for student in new_dict["students"]:
            new_list.append(student.__dict__)
        new_dict["students"] = new_list

        inst_list = list()
        for instructor in new_dict["instructors"]:
            inst_list.append(instructor.__dict__)
        new_dict["instructors"] = inst_list

        print(json.dumps(new_dict, indent=2))

    def __repr__(self):
        return f'{self.name}'
