import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        box = QComboBox()
        box.addItems(["One", "Two", "Three"])

        box.currentIndexChanged.connect(self.index_changed)
        box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(box)

    def index_changed(self, index):
        print(index)

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
