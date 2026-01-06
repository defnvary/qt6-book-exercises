from layout_colorwidget import Color
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()
        layout.addWidget(Color("green"))  # last widget (top of the stack apparantely)
        layout.addWidget(Color("red"))
        layout.addWidget(Color("black"))
        layout.addWidget(Color("violet"))

        layout.setCurrentIndex(3)  # chooses "violet" otherwise green will be shown
        # layout.setCurrentWidget can be used for choosing widgets in the same manner

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
