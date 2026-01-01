import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # or widget = QDoubleSpinBox()
        #

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # or widget.setRange(-10, 3)
        #
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  # or 0.5 for QDoubleSpinBox

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, value):
        print(value)

    def value_changed_str(self, string):
        print(string)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
