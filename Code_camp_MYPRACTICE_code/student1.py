class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa

    def honour_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
