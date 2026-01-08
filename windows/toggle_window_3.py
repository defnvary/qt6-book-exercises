# lately its been on my brain would you mind letting me know if hours don't turn into days
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
        self.label = QLabel("QWidget Window % d" % randint(1, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Show / Hide window app")
        self.w = AnotherWindow()
        button = QPushButton("Push me to toggle window")
        button.clicked.connect(self.toggle_window)
        self.setCentralWidget(button)

    def toggle_window(self):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
