import sys

from layout_colorwidget import Color
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("blue"), 0, 1)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("yellow"), 1, 2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
