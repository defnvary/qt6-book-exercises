import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Click Me!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        print("clicked")

        button = QMessageBox.question(self, "Question Dialog", "The longer message")

        if button == QMessageBox.StandardButton.Yes:
            print("yess")
        else:
            print("no")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
