import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    this 'window' is a qwidget. if it has no parent,
    it will appear as a free-floating window
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self):
        self.window = AnotherWindow()
        self.window.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
