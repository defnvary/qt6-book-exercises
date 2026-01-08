import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = AnotherWindow()
        button = QPushButton("Press to open a new window")
        button.clicked.connect(self.show_new_window)
        self.setCentralWidget(button)

    def show_new_window(self):
        self.w.show()


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()
