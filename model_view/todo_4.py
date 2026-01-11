import sys

from MainWindow import Ui_MainWindow
from PySide6 import QtGui
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()

        self.todos = todos or []

        self.tick = QtGui.QImage("./tick.png")

    def rowCount(self, index):
        return len(self.todos)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return self.tick


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
            index = indexes[0]
            row = index.row()

            del self.model.todos[row]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()

            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)

            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
