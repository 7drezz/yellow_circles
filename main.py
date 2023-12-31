import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.button = QPushButton('Тык', self)
        self.button.resize(141, 41)
        self.button.move(240, 360)
        self.flag = None

        self.button.clicked.connect(self.function)

    def function(self):
        self.flag = True
        self.update()

    def paintEvent(self, a0):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.flag = False

    def draw(self, qp):
        x = random.randint(100, 400)
        y = random.randint(100, 200)
        r = random.randint(1, 90)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(x, y, r, r)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())
