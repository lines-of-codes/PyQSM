# This Python file uses the following encoding: utf-8
import subprocess
import webbrowser
import platform
import re
import os

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QMessageBox
from ui_manageserver import Ui_ManageServer
from Constants import LOADER_ICONS
from ServerProperties import ServerProperties

class ProcessOutputChecker(QObject):
    newOutput = Signal(str)
    processFinished = Signal()

    def check(self, process):
        while True:
            output = process.stdout.readline()
            if process.poll() is not None and output == "":
                self.processFinished.emit()
                break
            if output:
                self.newOutput.emit(output)


class ManageServer(QtWidgets.QWidget):
    startOutputCheck = Signal(subprocess.Popen)

    def __init__(self, parent, serverData):
        super().__init__(parent)
        self.ui = Ui_ManageServer()
        self.ui.setupUi(self)

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

        # Initialize the widgets with saved data
        self.serverData = serverData
        self.ui.serverLabel.setText(serverData["name"])
        self.ui.backupList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.serverInfoLabel.setText(f'{serverData["loaderType"]} {serverData["minecraftVersion"]} Build {serverData["loaderVersion"]}')
        self.ui.modLoaderIcon.setPixmap(QtGui.QPixmap(LOADER_ICONS[serverData["loaderType"]]))

        self.ui.initialHeapSizeSlider.valueChanged.connect(self.initialHeapSizeChange)
        self.ui.maxHeapSizeSlider.valueChanged.connect(self.maxHeapSizeChange)

        self.ui.serverToggleBtn.clicked.connect(self.startButtonClicked)
        self.ui.openServerDirBtn.clicked.connect(self.openServerDir)

    def openServerDir(self):
        PLATFORMS = {
            "Linux": lambda f: 'xdg-open "%s"' % f,
            "Darwin": lambda f: 'open "%s"' % f,
            "Windows": lambda f: 'explorer "%s"' % f
        }

        jarFile = self.serverData["jarFileLocation"]

        if not os.path.isfile(jarFile):
            return QMessageBox.critical(self, "Jar file location invalid", "The Minecraft server's jar file is missing in the path specified. Please change the path or redownload the server jar file.")

        os.system(PLATFORMS[platform.system()](os.path.dirname(jarFile)))

    def detectJavaVersion(self, javaLocation="java"):
        proc = subprocess.run([javaLocation, "-version"], capture_output=True)
        match = re.search('".+"', str(proc.stderr)).match
        return match.strip('"')

    def initialHeapSizeChange(self, value):
        num = round(value / 1024, 1)

        if value % 1024 == 0:
            num = int(num)

        self.ui.initialHeapValueLabel.setText(f"({num}GB)")

        if value > self.ui.maxHeapSizeSlider.value():
            self.ui.maxHeapSizeSlider.setValue(value)

    def maxHeapSizeChange(self, value):
        num = round(value / 1024, 1)

        if value % 1024 == 0:
            num = int(num)

        self.ui.maxHeapValueLabel.setText(f"({num}GB)")

    def agreeEula(self, eula: ServerProperties, filePath: str):
        eula.values["eula"] = True
        with open(filePath, "w") as f:
            f.write(str(eula))

        self.eulaAgreed = True

    def startButtonClicked(self, serverOffline):
        if not serverOffline:
            print("Shutting down server...")

            self.ui.serverToggleBtn.setEnabled(False)
            self.ui.restartBtn.setEnabled(False)

            self.process.terminate()
            return

        print("Starting up server...")

        if not os.path.isfile(self.serverData["jarFileLocation"]):
            return QMessageBox.critical(self, "Jar file location invalid", "The Minecraft server's jar file is missing in the path specified. Please change the path or redownload the server jar file.")

        self.jarDir = os.path.dirname(self.serverData["jarFileLocation"])
        self.eulaAgreed = False
        eulaFile = f"{self.jarDir}/eula.txt"

        with open(eulaFile, "r") as f:
            eula = ServerProperties()
            eula.parse(str(f.read()))
            if eula.values["eula"] == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                msg.setText("You need to agree to the Minecraft EULA in order to start the server.")
                msg.addButton("View EULA", QMessageBox.ActionRole).clicked.connect(lambda: webbrowser.open("https://aka.ms/MinecraftEULA"))
                msg.addButton("I agree", QMessageBox.YesRole).clicked.connect(lambda: self.agreeEula(eula, eulaFile))
                msg.addButton("Stop Server", QMessageBox.NoRole)
                msg.exec()
            elif eula.values["eula"] == True:
                self.eulaAgreed = True

        if not self.eulaAgreed:
            return

        args = ["java", f"-Xms{int(self.ui.initialHeapSizeSlider.value())}M", f"-Xmx{int(self.ui.maxHeapSizeSlider.value())}M", "-jar", self.serverData["jarFileLocation"], "nogui"]

        self.ui.serverLog.clear()
        self.ui.serverLog.insertPlainText(f"Running: {' '.join(args)}\n")

        self.process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=self.jarDir)

        self.processOutputThread = QThread()
        self.processOutputChecker = ProcessOutputChecker()

        self.processOutputChecker.moveToThread(self.processOutputThread)
        self.startOutputCheck.connect(self.processOutputChecker.check)
        self.processOutputThread.finished.connect(self.processOutputChecker.deleteLater)
        self.processOutputChecker.newOutput.connect(self.handleProcessOutput)
        self.processOutputChecker.processFinished.connect(self.handleProcessFinished)
        self.processOutputChecker.processFinished.connect(self.processOutputThread.quit)

        self.processOutputThread.start()
        self.startOutputCheck.emit(self.process)

        self.ui.serverStateLabel.setText("ONLINE")
        self.ui.serverToggleBtn.setText("Stop")
        self.ui.restartBtn.setEnabled(True)

    @Slot(str)
    def handleProcessOutput(self, output):
        self.ui.serverLog.insertPlainText(output)

    @Slot()
    def handleProcessFinished(self):
        self.ui.serverStateLabel.setText("OFFLINE")
        self.ui.serverToggleBtn.setChecked(False)
        self.ui.serverToggleBtn.setEnabled(True)
        self.ui.serverToggleBtn.setText("Start")
