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
        # idx = self.model.fieldIndex("Milliseconds")

        # self.model.setSort(idx, Qt.DescendingOrder)
        # self.model.setHeaderData(1, Qt.Horizontal, "Name")
        # self.model.setHeaderData(2, Qt.Horizontal, "Album (ID)")
        # self.model.setHeaderData(4, Qt.Horizontal, "Media Type (ID)")
        # self.model.setHeaderData(5, Qt.Horizontal, "Genre (ID)")
        # self.model.setHeaderData(6, Qt.Horizontal, "Composer")
        #
        # this can be used too
        #
        column_titles = {
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
            "Compose": "Composer",
        }

        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal, t)

        # this only removes columns from the view, not from the actual db
        # remove columns you don't want to display (using column index)
        self.model.removeColumns(2, 5)

        # using column name
        columns_to_remove = ["name", "something"]

        for cn in columns_to_remove:
            idx = self.model.fieldIndex(cn)
            self.model.removeColumns(idx, 1)

        self.model.select()

        self.table = QTableView()
        self.table.setModel(self.model)

        self.setMinimumSize(QSize(1024, 600))

        self.setCentralWidget(self.table)


window = MainWindow()
window.show()

app.exec()
