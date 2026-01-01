import sys

from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

        self.setWindowTitle("My App")

    def item_changed(self, item):  # not an index item is QListItem object
        print(item.text())

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
