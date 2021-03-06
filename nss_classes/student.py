from .nss import NSS


class Student(NSS):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises_list = list()


    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'
