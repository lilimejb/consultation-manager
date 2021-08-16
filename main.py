from db_works.data import db_session

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
            self.person_info.setStyleSheet(STYLE1)
            self.available_dates.setStyleSheet(STYLE1)
            self.teachers.setStyleSheet(STYLE1)
            self.create_order.setStyleSheet(STYLE1)
            self.date_choose.setStyleSheet(STYLE1)
            self.error_label.setStyleSheet(STYLE1)
            self.teachers_choose.setStyleSheet(STYLE1)
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
            self.person_info.setStyleSheet(STYLE2)
            self.available_dates.setStyleSheet(STYLE2)
            self.teachers.setStyleSheet(STYLE2)
            self.create_order.setStyleSheet(STYLE2)
            self.date_choose.setStyleSheet(STYLE2)
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