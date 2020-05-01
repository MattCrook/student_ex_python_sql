
import json
from .nss import NSS


class Instructor(NSS):
    def __init__(self, first_name, last_name,  slack_handle, specialty, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def __repr__(self):
        return f'{self.first_name} {self.last_name} has the specialty of {self.specialty} and teaches cohort {self.cohort}.'
