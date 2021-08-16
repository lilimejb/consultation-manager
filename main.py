from db_works.data import db_session
from db_works.data.teachers import Teacher
from db_works.data.students import Student
from main_classes import Teachers, Students

import datetime
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtSql import *

db_session.global_init("db_works/db/consultation.db")

BACKGROUND_STYLE1 = """background-color: #D7FDF0;"""
BACKGROUND_STYLE2 = """background-color: #E4DFDA;"""

STYLE1 = """
    *{
	    background:linear-gradient(to bottom, #62c1e0 5%, #019ad2 100%);
	    background-color:#B2FFD6;
	    border-radius:6px;
	    border:1px solid #057fd0;
	    color:#AA78A6;
	    font-family:Arial;
	    font-size:15px;
	    font-weight:bold;
	    padding:6px 6px;
	    text-decoration:none;
    }
        *:hover {
	    background:linear-gradient(to bottom, #019ad2 5%, #62c1e0 100%);
	    background-color:#B4D6D3;
    }
    *:active {
	    position:relative;
	    top:1px;
    }
"""

STYLE2 = """*{
	background:linear-gradient(to bottom, #62c1e0 5%, #019ad2 100%);
	background-color:#824670;
	border-radius:6px;
	border:1px solid #FFFFFF;
	color:#E4DFDA;
	font-family:Arial;
	font-size:15px;
	font-weight:bold;
	padding:6px 6px;
	text-decoration:none;
}
*:hover {
	background:linear-gradient(to bottom, #019AD2 5%, #62C1E0 100%);
	background-color:#BDA0BC;
}
*:active {
	position:relative;
	top:1px;
}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.stack.setCurrentIndex(0)

        self.green.triggered.connect(self.change_theme)
        self.cream.triggered.connect(self.change_theme)

        self.help_text.hide()
        self.help_button.clicked.connect(self.help_show)

        self.choose_teacher.currentTextChanged.connect(self.show_teacher_info)
        self.subject_choose.currentTextChanged.connect(self.set_teachers)
        self.teacher_choose.currentTextChanged.connect(self.set_date)
        self.create_order.clicked.connect(self.show_order_info)

        self.go_home_1.clicked.connect(self.set_main)
        self.go_home_3.clicked.connect(self.set_main)
        self.go_home_2.clicked.connect(self.set_main)
        self.go_teacher_page.clicked.connect(self.set_teacher_page)
        self.go_student_page.clicked.connect(self.set_student_page)
        self.go_admin_page.clicked.connect(self.set_admin_page)

    def set_main(self):
        self.stack.setCurrentIndex(0)

    def set_teacher_page(self):
        self.stack.setCurrentIndex(1)
        db_sess = db_session.create_session()
        teachers = db_sess.query(Teacher).all()
        self.choose_teacher.addItem('')
        for teacher in teachers:
            self.choose_teacher.addItem(teacher.name)

    def show_teacher_info(self):
        sender = self.sender().currentText()
        db_sess = db_session.create_session()
        if sender:
            teacher = db_sess.query(Teacher).filter(Teacher.name == sender).all()[0]
            teacher = Teachers(teacher.name, [], teacher.subjects.split(), teacher.available_dates.split(', '))

            info_text = f'                 Учитель {teacher.name}\n '

            info_text += f'\n Преподаватель по предметам: \n'
            for subject in teacher.get_subject():
                info_text += f'\t {subject} \n'

            info_text += f'\n Время для записи: \n'
            for date in teacher.get_dates():
                info_text += f'\t {date} \n'

            self.teacher_info.setText(info_text)

    def set_student_page(self):
        self.stack.setCurrentIndex(2)
        db_sess = db_session.create_session()
        teachers = db_sess.query(Teacher).all()
        subjects = list()
        for teacher in teachers:
            subjects.extend(teacher.subjects.split())
        subjects = list(set(subjects))
        self.subject_choose.addItem('')
        for subject in subjects:
            self.subject_choose.addItem(subject)

    def set_teachers(self):
        sender = self.sender().currentText()
        db_sess = db_session.create_session()

        if sender:
            [self.teacher_choose.removeItem(i) for i in range(self.teacher_choose.count() + 1)]
            self.teacher_choose.addItem('')
            self.teacher_choose.addItem('')
            teachers = db_sess.query(Teacher).all()
            [self.teacher_choose.addItem(teacher.name) for teacher in teachers if sender in teacher.subjects]
            self.teacher_choose.removeItem(0)

    def set_date(self):
        sender = self.sender().currentText()
        db_sess = db_session.create_session()

        if sender:
            [self.date_choose.removeItem(i) for i in range(self.date_choose.count() + 1)]
            self.date_choose.addItem('')
            self.date_choose.addItem('')
            teachers = db_sess.query(Teacher).all()
            [self.date_choose.addItem(date) for teacher in teachers for date in teacher.available_dates.split(', ')  if sender == teacher.name]
            self.date_choose.removeItem(0)

    def show_order_info(self):
        name = self.name_inter.text()
        date = self.date_choose.currentText()
        teacher = self.teacher_choose.currentText()
        subject = self.subject_choose.currentText()
        teacher = Teachers(teacher, name, subject, [date])

        info_text = f'\t\t\t\t\tУченик {teacher.get_students()}\n' + \
                    f'Записан к {teacher.get_name()} на консультацию по предмету {teacher.get_subject()}\n' + \
                    f'Дата встречи: {teacher.get_dates()[0]}'

        self.order_info.setText(info_text)

    def set_admin_page(self):
        self.stack.setCurrentIndex(3)

    def help_show(self):
        if self.sender().text().endswith('⯈'):
            self.help_text.show()
            self.help_button.setText('Справка ⯅')
        else:
            self.help_button.setText('Справка ⯈')
            self.help_text.hide()

    def change_theme(self):
        sender = self.sender().text()
        if sender == 'Зелёная':
            self.go_home_1.setStyleSheet(STYLE1)
            self.go_home_3.setStyleSheet(STYLE1)
            self.go_home_2.setStyleSheet(STYLE1)
            self.go_admin_page.setStyleSheet(STYLE1)
            self.go_student_page.setStyleSheet(STYLE1)
            self.go_teacher_page.setStyleSheet(STYLE1)
            self.help_button.setStyleSheet(STYLE1)
            self.help_text.setStyleSheet(STYLE1)
            self.choose_teacher.setStyleSheet(STYLE1)
            self.teacher_info.setStyleSheet(STYLE1)
            self.available_dates.setStyleSheet(STYLE1)
            self.teachers.setStyleSheet(STYLE1)
            self.create_order.setStyleSheet(STYLE1)
            self.date_choose.setStyleSheet(STYLE1)
            self.subject_choose.setStyleSheet(STYLE1)
            self.teachers_choose.setStyleSheet(STYLE1)
            self.error_label.setStyleSheet(STYLE1)
            self.teacher_choose.setStyleSheet(STYLE1)
            self.info_view.setStyleSheet(STYLE1)
            self.setStyleSheet(BACKGROUND_STYLE1)
        elif sender == 'Кремовая':
            self.go_home_1.setStyleSheet(STYLE2)
            self.go_home_3.setStyleSheet(STYLE2)
            self.go_home_2.setStyleSheet(STYLE2)
            self.go_admin_page.setStyleSheet(STYLE2)
            self.go_student_page.setStyleSheet(STYLE2)
            self.go_teacher_page.setStyleSheet(STYLE2)
            self.help_button.setStyleSheet(STYLE2)
            self.help_text.setStyleSheet(STYLE2)
            self.choose_teacher.setStyleSheet(STYLE2)
            self.teacher_info.setStyleSheet(STYLE2)
            self.available_dates.setStyleSheet(STYLE2)
            self.teachers.setStyleSheet(STYLE2)
            self.create_order.setStyleSheet(STYLE2)
            self.date_choose.setStyleSheet(STYLE2)
            self.subject_choose.setStyleSheet(STYLE2)
            self.teacher_choose.setStyleSheet(STYLE2)
            self.error_label.setStyleSheet(STYLE2)
            self.teachers_choose.setStyleSheet(STYLE2)
            self.info_view.setStyleSheet(STYLE2)
            self.setStyleSheet(BACKGROUND_STYLE2)



def error_catcher(exctype, value, tb):
    print('My Error Information')
    print('Type:', exctype)
    print('Value:', value)
    print('Traceback:', tb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = error_catcher
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())