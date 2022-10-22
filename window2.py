from PyQt5.QtCore import Qt, QTime, QTimer
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
        self.btn_test1.clicked.connect(self.start_test1)
        self.btn_test2.clicked.connect(self.start_test2)
        self.btn_test3.clicked.connect(self.start_test3)

    def start_test1(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def timer1_event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString('hh:mm:ss'))
        self.lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.lb_timer.setStyleSheet('color: rgb(0, 0, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def start_test2(self):
        self.time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)
    
    def timer2_event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString('hh:mm:ss')[6:8])
        self.lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.lb_timer.setStyleSheet('color: rgb(0, 0, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
        
    def start_test3(self):
        self.time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_event)
        self.timer.start(1000)

    def timer3_event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString('hh:mm:ss'))
        self.lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        if self.time.toString('hh:mm:ss') == '00:00:59':
            self.lb_timer.setStyleSheet('color: rgb(0, 255, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:45':
            self.lb_timer.setStyleSheet('color: rgb(0, 0, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:15':
            self.lb_timer.setStyleSheet('color: rgb(0, 255, 0);')
        
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.lb_timer.setStyleSheet('color: rgb(0, 0, 0);')
            self.timer.stop()
        
        

    