class Teacher:
    def __init__(self):
        self.available_dates = list()
        self.name = str()
        self.students = dict()

    def get_name(self):
        return self.name

    def get_dates(self):
        return self.available_dates


class Student:
    def __init__(self):
        self.name = str()
        self.wanted_date = None
        self.teacher_name = str()

    def get_name(self):
        return self.name

    def get_date(self):
        return self.wanted_date

    def get_teacher_name(self):
        return self.teacher_name