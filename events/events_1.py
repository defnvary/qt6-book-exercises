import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText("mouse move event")

    def mousePressEvent(self, event):
        self.label.setText("mouse press event")

    def mouseReleaseEvent(self, event):
        self.label.setText("mouse release event")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("mouse double click event")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
