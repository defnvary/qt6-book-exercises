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

        # QMainWindow.__init__(self)
        # Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)

        # connect the button
        self.addButton.pressed.connect(self.add)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit.todoEdit
        and then clearing it
        """
        text = self.todoEdit.text()
        text = text.strip()  # remove whitespace from the ends of the string

        if text:  # don't add empty strings
            # access the list via the model
            self.model.todos.append((False, text))
            # trigger refresh
            self.model.layoutChanged.emit()
            # employ the input
            self.todoEdit.setText("")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
