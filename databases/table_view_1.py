import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table View")

        self.model = QSqlTableModel(db=db)
        self.model.setTable("Track")
        idx = self.model.fieldIndex("Milliseconds")
        self.model.setSort(idx, Qt.DescendingOrder)
        self.model.select()

        self.table = QTableView()
        self.table.setModel(self.model)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


window = MainWindow()
window.show()

app.exec()
