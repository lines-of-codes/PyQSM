# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
import AzulMetadata
from ui_JREDownloadDialog import Ui_Dialog

class JREDownloadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.loadJREList()

    def loadJREList(self):
        self.listAzulJRE()

    def listAzulJRE(self):
        self.ui.jreList.addItems(AzulMetadata.listJRE(self.ui.jreVersionSelect.currentText()))
