class Teachers:
    def __init__(self, name, students, subjects, available_dates):
        self.available_dates = []
        for date_time in available_dates:
            date, time = date_time.split()
            date = date.split('-')
            date_time = f'{date[2]}-{date[1]}-{date[0]} {time}'
            self.available_dates.append(date_time)

        self.name = name
        self.students = students
        self.subjects = subjects

    def get_name(self):
        return self.name

    def get_dates(self):
        return self.available_dates

    def get_subject(self):
        return self.subjects

    def get_students(self):
        return self.students


class Students:
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