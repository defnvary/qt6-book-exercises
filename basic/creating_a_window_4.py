import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# subclass mainwindow to customize your applications main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me")

        # set central widget of the window
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
