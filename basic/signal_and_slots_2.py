from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Push Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # set the central widget of the window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You Already Clicked Me!")
        self.button.setEnabled(False)

        # also change the window title
        self.setWindowTitle("My Oneshot App")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
