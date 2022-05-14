import csv
import sys

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from res.ui_index import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.action_new_project.triggered.connect(self.new_project)
        self.csvbutton.clicked.connect(self.do_posts)

    def do_posts(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
        model = QStandardItemModel()

        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        with open(path, "r") as fileInput:
            for i, row in enumerate(csv.reader(fileInput)):
                if i == 0:
                    model.setHorizontalHeaderLabels([r.strip().strip('"') for r in row])
                else:
                    items = [
                        QStandardItem(field.strip())
                        for field in row
                    ]
                    model.appendRow(items)

        self.tableView.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
