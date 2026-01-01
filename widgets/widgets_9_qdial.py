import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(2)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, value):
        print(value)

    def slider_moved(self, pos):
        print(pos)

    def slider_pressed(self):
        print("Pressed")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
