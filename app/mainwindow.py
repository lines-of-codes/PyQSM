# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow
from CreateServerPage import CreateServerPage

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.newServerBtn.clicked.connect(self.newServerBtnClicked)

    def newServerBtnClicked(self):
        tabIndex = self.ui.tabWidget.addTab(CreateServerPage(), QIcon(":/imgs/icons/plus.svg"), "Create new server")
        self.ui.tabWidget.setCurrentIndex(tabIndex)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
