import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

loader = QUiLoader()

app = QApplication(sys.argv)

window = loader.load("./mainwindow.ui", None)
window.show()

app.exec()
