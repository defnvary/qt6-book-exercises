import sys

from MainWindow import Ui_MainWindow

# import ListModel
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow


# tag::model[]
class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()

        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)


# end::model[]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos=[(False, "my first todo")])
        self.todoView.setModel(self.model)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
