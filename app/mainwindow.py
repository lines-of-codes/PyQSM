# This Python file uses the following encoding: utf-8
import json
import sys
import os

from PySide6 import QtAsyncio
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTabBar, QMessageBox, QStyleFactory

from ui_mainwindow import Ui_MainWindow
from CreateServerPage import CreateServerPage
from ManageServer import ManageServer
from Constants import LOADER_ICONS
from JREDownloadDialog import JREDownloadDialog

aboutText = """PyQSM is a software for managing Minecraft servers.

This software uses Qt and is licensed under the GPLv3 license."""

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.newServerBtn.clicked.connect(self.newServerBtnClicked)

        self.ui.actionInstall_Java.triggered.connect(self.jreDialog)

        self.ui.actionAbout_PyQSM.triggered.connect(lambda: QMessageBox.about(self, "About PyQSM", aboutText))
        self.ui.actionAbout_Qt.triggered.connect(lambda: QMessageBox.aboutQt(self, "About Qt"))

        tabBar = self.ui.tabWidget.tabBar()
        tabBar.setTabButton(0, QTabBar.ButtonPosition.LeftSide, None)
        tabBar.setTabButton(0, QTabBar.ButtonPosition.RightSide, None)
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

        serverListDir = f"{os.getcwd()}/servers"

        if not os.path.isdir(serverListDir):
            os.mkdir(serverListDir)

        self.serverListFile = f"{serverListDir}/servers.json"
        # Server List File Schema
        # {
        #   serverName: {
        #      "name": serverName,
        #      "jarFileLocation": jarFileLocation,
        #      "minecraftVersion": minecraftVersion,
        #      "loaderType": loader,
        #      "loaderVersion": selectedBuild
        #   }
        # }
        self.loadServerList()

        self.ui.refreshBtn.clicked.connect(self.loadServerList)
        self.ui.serverList.itemDoubleClicked.connect(self.serverDoubleClicked)

    def jreDialog(self):
        jreDialog = JREDownloadDialog(self)
        jreDialog.exec()

    def newServerBtnClicked(self):
        tabIndex = self.ui.tabWidget.addTab(CreateServerPage(self), QIcon(":/imgs/icons/plus.svg"), "Create new server")
        self.ui.tabWidget.setCurrentIndex(tabIndex)

    def loadServerList(self):
        self.ui.serverList.clear()
        if os.path.isfile(self.serverListFile):
            with open(self.serverListFile, "r") as f:
                self.serverList = json.loads(f.read())
                self.ui.serverList.addItems(self.serverList.keys())

    def serverDoubleClicked(self, server):
        serverData = self.serverList[server.text()]
        icon = LOADER_ICONS.get(serverData["loaderType"])
        if icon is None:
            tabIndex = self.ui.tabWidget.addTab(ManageServer(self, serverData), serverData["name"])
        else:
            tabIndex = self.ui.tabWidget.addTab(ManageServer(self, serverData), QIcon(LOADER_ICONS[serverData["loaderType"]]), serverData["name"])
        self.ui.tabWidget.setCurrentIndex(tabIndex)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))
    widget = MainWindow()
    widget.show()

    QtAsyncio.run()
