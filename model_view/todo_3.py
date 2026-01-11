import sys

from MainWindow import Ui_MainWindow
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow


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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("To Do App")
        self.model = TodoModel()
        self.todoView.setModel(self.model)

        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.todoEdit.text()
        text = text.strip()

        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")

    def delete(self):
        indexes = self.todoView.selectedIndexes()

        if indexes:
            # indexes is a list of a single item in single select mode
            index = indexes[0]
            # remove the item and refresh
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()

            # clear the selection (as it is no longer valid)
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()

            status, text = self.model.todos[row]
            # print(text)

            self.model.todos[row] = (True, text)

            # .dataChanged takes top-left and bottom-right which are equal
            self.model.dataChanged.emit(index, index)
            # clear the selection as it is no longer valid
            self.todoView.clearSelection()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
