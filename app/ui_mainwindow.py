# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)
import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 525)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(48, 48, 48, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(72, 72, 72, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(60, 60, 60, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(24, 24, 24, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(204, 204, 204, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(24, 24, 24, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(34, 34, 34, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush10)
        MainWindow.setPalette(palette)
        self.actionAbout_PyQSM = QAction(MainWindow)
        self.actionAbout_PyQSM.setObjectName(u"actionAbout_PyQSM")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionInstall_Java = QAction(MainWindow)
        self.actionInstall_Java.setObjectName(u"actionInstall_Java")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 701, 481))
        self.tabWidget.setTabsClosable(True)
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.newServerBtn = QPushButton(self.homeTab)
        self.newServerBtn.setObjectName(u"newServerBtn")
        self.newServerBtn.setGeometry(QRect(10, 10, 101, 25))
        self.newServerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/imgs/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newServerBtn.setIcon(icon)
        self.newServerBtn.setIconSize(QSize(12, 12))
        self.importServerBtn = QPushButton(self.homeTab)
        self.importServerBtn.setObjectName(u"importServerBtn")
        self.importServerBtn.setGeometry(QRect(120, 10, 121, 25))
        icon1 = QIcon()
        icon1.addFile(u":/imgs/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importServerBtn.setIcon(icon1)
        self.importServerBtn.setIconSize(QSize(12, 12))
        self.serverList = QListWidget(self.homeTab)
        self.serverList.setObjectName(u"serverList")
        self.serverList.setGeometry(QRect(10, 40, 671, 391))
        self.refreshBtn = QPushButton(self.homeTab)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(569, 10, 111, 25))
        icon2 = QIcon()
        icon2.addFile(u":/imgs/icons/reload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon2)
        self.refreshBtn.setIconSize(QSize(12, 12))
        self.tabWidget.addTab(self.homeTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 22))
        self.menuJava = QMenu(self.menuBar)
        self.menuJava.setObjectName(u"menuJava")
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuJava.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuJava.addAction(self.actionInstall_Java)
        self.menuAbout.addAction(self.actionAbout_PyQSM)
        self.menuAbout.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quick Minecraft Server Manager", None))
        self.actionAbout_PyQSM.setText(QCoreApplication.translate("MainWindow", u"About PyQSM", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionInstall_Java.setText(QCoreApplication.translate("MainWindow", u"Install Java", None))
        self.newServerBtn.setText(QCoreApplication.translate("MainWindow", u" New server", None))
        self.importServerBtn.setText(QCoreApplication.translate("MainWindow", u" Import Server", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u" Refresh List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuJava.setTitle(QCoreApplication.translate("MainWindow", u"Java", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

