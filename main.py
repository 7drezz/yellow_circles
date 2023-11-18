import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.function)
        self.flag = None

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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, r, r)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())
