from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class Second(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.flag = False
        self.krugi = []
        self.pushButton.clicked.connect(self.click)

    def paintEvent(self, a0) -> None:
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        color = QColor.fromRgb(255, 255, 0)
        qp.setBrush(QBrush(color))
        qp.setPen(QPen(color))
        for x, y, r in self.krugi:
            qp.drawEllipse(x, y, r, r)

    def click(self):
        self.flag = True
        self.krugi.append((randint(0, self.geometry().width()), randint(0, self.geometry().height()),
                           randint(0, 80)))
        self.update()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = Second()
    ex.show()
    sys.exit(app.exec())