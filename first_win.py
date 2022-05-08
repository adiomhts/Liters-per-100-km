from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

from second_win import Result

class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle("ввод")
        self.resize(500, 500)

    def initUI(self):
        self.text_hello = QLabel("данная программа поможет расчитать расход топлива")
        self.description = QLabel("Ниже вы можете ввести данные")
        self.btn_next = QPushButton('Посчитать')
        self.text_liters = QLabel('сюда введите потраченные литры')
        self.liters = QLineEdit()
        self.text_km = QLabel('сюда введите пройденное растояние')
        self.km = QLineEdit()

        
        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.text_hello, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.description, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.text_liters, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.liters, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.text_km, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.km, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.w = Result(int(self.liters.text()), int(self.km.text()))


app = QApplication([])

window = FirstWin()

app.exec_()
