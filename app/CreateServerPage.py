# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from ui_createserverpage import Ui_CreateServerPage
import PaperMCApi
import PurpurMCApi
import asyncio
import shutil
import json
import re
import os

class CreateServerPage(QtWidgets.QWidget):
    def __init__(self, parent):
        """
        This class is meant to be created by the MainWindow class
        and the parent is hard coded to be the MainWindow.
        """

        super().__init__(parent)
        self.ui = Ui_CreateServerPage()
        self.ui.setupUi(self)

        self.ui.browseFileBtn.clicked.connect(self.onBrowseFileBtnClicked)
        self.ui.loaderChoice.currentTextChanged.connect(self.onLoaderChoiceChange)
        self.ui.minecraftVersionList.currentTextChanged.connect(lambda text: asyncio.ensure_future(self.onMinecraftVersionChange(text)))

        self.ui.nextBtn.clicked.connect(self.nextBtnClicked)

        self.win = parent
        self.IS_CREATING_SERVER = False

    def nextBtnClicked(self):
        if self.IS_CREATING_SERVER:
            return QMessageBox.critical(self, "Server creation process is already running", "A server creation process is already running. Please wait before attempting to make another server.")

        serverName = self.ui.serverName.text().strip()
        MISSING_INFO = "Information required"
        if not serverName or re.search(r"[@_!#$%^&*()<>?/\|}{~:]", serverName):
            return QMessageBox.critical(self, MISSING_INFO, "The input cannot contain any special symbols and must contain at least one character that is not a whitespace")

        jarFileLocation = self.ui.jarFileLocation.text().strip()
        selectedBuild = self.ui.buildList.currentItem()

        if selectedBuild is None:
            if not jarFileLocation:
                return QMessageBox.critical(self, MISSING_INFO, "No Minecraft server file is selected.")
            if not os.path.isfile(jarFileLocation):
                return QMessageBox.critical(self, "Selected jar file does not exist", "The selected Minecraft server jar file does not exist.")

        selectedBuild = selectedBuild.text()

        serverListDir = f"{os.getcwd()}/servers"
        serverListFile = f"{serverListDir}/servers.json"
        serverList = {}

        if os.path.isfile(serverListFile):
            with open(serverListFile, "r") as f:
                serverList = json.loads(f.read())

        if serverList.get(serverName) is not None:
            return QMessageBox.critical(self, "Name conflict", "A server with an existing name already exist. Please choose another name for the server. Either add some prefix, suffix, think of an entirely new name, or delete the existing server which has this name.")

        self.IS_CREATING_SERVER = True

        self.win.statusBar().showMessage("Creating server, please wait.")

        minecraftVersion = self.ui.minecraftVersionList.currentItem().text()
        loader = self.ui.loaderChoice.currentText()

        serverDir = f"{serverListDir}/{serverName}"

        # Skip the directory creation process if it somehow already exists
        if not os.path.isdir(serverDir):
            os.mkdir(serverDir)

        if not jarFileLocation:
            handler = getattr(CreateServerPage, f"handleDownload{loader}", None)

            if handler is None:
                return QMessageBox.critical(self, "This is illegal", "You just did something illegal. A build is selected but that build does not exist.")

            self.win.statusBar().showMessage("Downloading server file...")
            jarFileLocation = f"{serverDir}/{loader}-{minecraftVersion}-{selectedBuild}.jar"
            handler(minecraftVersion, selectedBuild, jarFileLocation)
        else:
            self.win.statusBar().showMessage("Copying server file...")
            newLocation = f"{serverDir}/{loader}-{minecraftVersion}-{selectedBuild}.jar"
            shutil.copyfile(jarFileLocation, newLocation)
            jarFileLocation = newLocation

        self.win.statusBar().showMessage("Finalizing server creation...")

        serverList[serverName] = {
            "name": serverName,
            "jarFileLocation": jarFileLocation,
            "minecraftVersion": minecraftVersion,
            "loaderType": loader,
            "loaderVersion": selectedBuild
        }

        with open(serverListFile, "w") as f:
            f.write(json.dumps(serverList))

        self.win.statusBar().clearMessage()

        tabWidget = self.win.ui.tabWidget
        tabWidget.removeTab(tabWidget.currentIndex())

        self.IS_CREATING_SERVER = False

    @staticmethod
    def handleDownloadPaper(minecraftVersion, build, location):
        PaperMCApi.downloadBuild(PaperMCApi.PAPER, minecraftVersion, build, location)

    @staticmethod
    def handleDownloadVelocity(minecraftVersion, build, location):
        PaperMCApi.downloadBuild(PaperMCApi.VELOCITY, minecraftVersion, build, location)

    @staticmethod
    def handleDownloadPurpur(minecraftVersion, build, location):
        PurpurMCApi.downloadBuild(minecraftVersion, build, location)

    def onBrowseFileBtnClicked(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select server .jar file", "", "JAR Archive (*.jar)")

        if fileName is None:
            return

        self.ui.jarFileLocation.setText(fileName)

    def onLoaderChoiceChange(self, loader):
        self.ui.minecraftVersionList.clear()
        self.ui.buildList.clear()

        handler = getattr(CreateServerPage, f"handleLoader{loader}", None)
        if handler is not None:
            asyncio.create_task(handler(self))

    async def handleLoaderVelocity(self):
        self.ui.minecraftVersionList.addItems(PaperMCApi.getAvailableMinecraftVersions(PaperMCApi.VELOCITY))

    async def handleLoaderPaper(self):
        self.ui.minecraftVersionList.addItems(PaperMCApi.getAvailableMinecraftVersions(PaperMCApi.PAPER))

    async def handleLoaderPurpur(self):
        self.ui.minecraftVersionList.addItems(PurpurMCApi.getAvailableMinecraftVersions())

    async def onMinecraftVersionChange(self, version):
        if not version:
            return

        currentLoader = self.ui.loaderChoice.currentText()
        self.ui.buildList.clear()

        handler = getattr(CreateServerPage, f"handleVersion{currentLoader}", None)
        if handler is not None:
            await handler(self, version)
            self.ui.buildList.setCurrentRow(0)

    async def handleVersionVelocity(self, minecraftVersion):
        self.ui.buildList.addItems(PaperMCApi.getAvailableBuilds(PaperMCApi.VELOCITY, minecraftVersion))

    async def handleVersionPaper(self, minecraftVersion):
        self.ui.buildList.addItems(PaperMCApi.getAvailableBuilds(PaperMCApi.PAPER, minecraftVersion))

    async def handleVersionPurpur(self, minecraftVersion):
        self.ui.buildList.addItems(PurpurMCApi.getAvailableBuilds(minecraftVersion))
