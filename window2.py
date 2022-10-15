from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from instr import *

class Win2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lb_name = QLabel(txt_name)
        self.le_name = QLineEdit(txt_hintname)
        
        self.lb_age = QLabel(txt_age)
        self.le_age = QLineEdit(txt_hintage)

        self.lb_test1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.le_test1 = QLineEdit(txt_hinttest1)

        self.lb_test2 = QLabel(txt_test2)
        self.btn_test2 = QPushButton(txt_starttest2)

        self.lb_test3 = QLabel(txt_test3)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.le_test2 = QLineEdit(txt_hinttest2)
        self.le_test3 = QLineEdit(txt_hinttest3)

        self.btn_next = QPushButton(txt_sendresults)

        self.lb_timer = QLabel(txt_timer)
        self.lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        

        #на лініЇ розташовують
        self.h_line = QHBoxLayout()
        self.v_line_l = QVBoxLayout()
        self.v_line_r = QVBoxLayout()

        #розташування віджетів
        self.v_line_l.addWidget(self.lb_name, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_name, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_name, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.lb_age, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_age, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.lb_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.lb_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.lb_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.le_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.v_line_r.addWidget(self.lb_timer, alignment=Qt.AlignCenter)
        
        self.h_line.addLayout(self.v_line_l)
        self.h_line.addLayout(self.v_line_r)
        self.setLayout(self.h_line)
        



    def connects(self):
        pass