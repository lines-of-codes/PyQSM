# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
import AzulMetadata
import AdoptiumAPI
from ui_JREDownloadDialog import Ui_Dialog
import asyncio

class JREDownloadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        asyncio.create_task(self.providerAzulJRE())

        self.jreName = "Zulu"
        self.ui.zulu.clicked.connect(lambda: asyncio.create_task(self.providerAzulJRE()))
        self.ui.temurin.clicked.connect(lambda: asyncio.create_task(self.providerEclipseJRE()))
        self.ui.amazon.clicked.connect(lambda: print("Amazon Coretto"))
        self.ui.microsoft.clicked.connect(lambda: print("Microsoft OpenJDK"))

        self.ui.jreVersionSelect.currentTextChanged.connect(self.jreVersionChange)

    async def providerAzulJRE(self):
        self.jreName = "Zulu"
        self.ui.jreList.clear()
        self.ui.jreList.addItems(AzulMetadata.listJRE(self.ui.jreVersionSelect.currentText()))

    async def providerEclipseJRE(self):
        self.jreName = "Temurin"
        self.ui.jreList.clear()
        if len(AdoptiumAPI.versions.keys()) == 0:
            AdoptiumAPI.getAvailableReleases()
        self.ui.jreVersionSelect.clear()
        self.ui.jreVersionSelect.addItems(list(AdoptiumAPI.versions.keys())[::-1])

    def providerAmazonJRE(self):
        pass

    def providerMicrosoftJRE(self):
        pass

    def jreVersionChange(self, text):
        handler = getattr(JREDownloadDialog, f"version{self.jreName}JRE", None)
        self.ui.jreList.clear()
        if handler is not None:
            asyncio.create_task(handler(self, text))

    async def versionZuluJRE(self, text):
        self.ui.jreList.addItems(AzulMetadata.listJRE(text))

    async def versionTemurinJRE(self, text):
        self.ui.jreList.addItems(AdoptiumAPI.listJRE(text))
