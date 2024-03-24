# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from ui_createserverpage import Ui_CreateServerPage
import PaperMCApi
import PurpurMCApi

class CreateServerPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateServerPage()
        self.ui.setupUi(self)
        self.ui.browseFileBtn.clicked.connect(self.onBrowseFileBtnClicked)
        self.ui.loaderChoice.currentIndexChanged.connect(self.onLoaderChoiceChange)
        self.ui.minecraftVersionList.currentTextChanged.connect(self.onMinecraftVersionChange)

    def onBrowseFileBtnClicked(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Select server .jar file", "", "JAR Archive (*.jar)")

        if fileName is None:
            return

        self.ui.jarFileLocation.setText(fileName)

    def onLoaderChoiceChange(self):
        currentChoice = self.ui.loaderChoice.currentText()
        self.ui.minecraftVersionList.clear()

        handler = getattr(CreateServerPage, f"handleLoader{currentChoice}", None)
        if handler is not None:
            handler(self)

    def handleLoaderVelocity(self):
        self.ui.minecraftVersionList.addItems(PaperMCApi.getAvailableMinecraftVersions(PaperMCApi.VELOCITY))

    def handleLoaderPaper(self):
        self.ui.minecraftVersionList.addItems(PaperMCApi.getAvailableMinecraftVersions(PaperMCApi.PAPER))

    def handleLoaderPurpur(self):
        self.ui.minecraftVersionList.addItems(PurpurMCApi.getAvailableMinecraftVersions())

    def onMinecraftVersionChange(self, version):
        if not version:
            return

        currentLoader = self.ui.loaderChoice.currentText()
        self.ui.buildList.clear()

        handler = getattr(CreateServerPage, f"handleVersion{currentLoader}", None)
        if handler is not None:
            handler(self, version)

    def handleVersionVelocity(self, minecraftVersion):
        self.ui.buildList.addItems(PaperMCApi.getAvailableBuilds(PaperMCApi.VELOCITY, minecraftVersion))

    def handleVersionPaper(self, minecraftVersion):
        self.ui.buildList.addItems(PaperMCApi.getAvailableBuilds(PaperMCApi.PAPER, minecraftVersion))

    def handleVersionPurpur(self, minecraftVersion):
        self.ui.buildList.addItems(PurpurMCApi.getAvailableBuilds(minecraftVersion))
