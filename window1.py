from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from instr import *
class Win1(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        pass
    def initUI(self):
        pass
    def connects(self):
        pass

app = QApplication([])

win1 = Win1()
app.exec_()