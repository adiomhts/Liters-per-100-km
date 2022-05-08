from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,


class Result(QWidget):
    def __init__(self, liters, km):
        super().__init__()
        self.liters = liters
        self.km = km
        self.set_appear()
        self.initUI()
        self.show()


    def set_appear(self):
        self.setWindowTitle("Результат")
        self.resize(500, 500)

    def initUI(self):

        liters_per_100km = (self.liters*100)/self.km
        liters_per_100km = round(liters_per_100km, 2)

        self.lpkm = QLabel('Ваш расход топлива:'+str(liters_per_100km)+'л/100км')


        self.v = QVBoxLayout()

        self.v.addWidget(self.lpkm, alignment=Qt.AlignCenter)

        self.setLayout(self.v)















