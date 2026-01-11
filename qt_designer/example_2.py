from random import randint

from MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # signals from ui elements can be connected as normal
        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        self.label.setText("%d" % randint(1, 6))


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
