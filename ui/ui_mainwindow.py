# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(451, 271)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(451, 271))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionOpen_Log = QAction(MainWindow)
        self.actionOpen_Log.setObjectName(u"actionOpen_Log")
        self.actionOpen_Log.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(font)
        self.actionUser_Guide = QAction(MainWindow)
        self.actionUser_Guide.setObjectName(u"actionUser_Guide")
        self.actionUser_Guide.setFont(font)
        self.actionLoad_File = QAction(MainWindow)
        self.actionLoad_File.setObjectName(u"actionLoad_File")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(2, 1, 447, 226))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.MainTab.setFont(font2)
        self.label = QLabel(self.MainTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 20, 65, 31))
        self.label.setFont(font1)
        self.addButton = QPushButton(self.MainTab)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(360, 20, 66, 31))
        self.addButton.setFont(font1)
        self.comboBox = QComboBox(self.MainTab)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(80, 20, 266, 31))
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFont(font2)
        self.comboBox.setEditable(True)
        self.textEdit = QTextEdit(self.MainTab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(-2, 70, 445, 131))
        self.textEdit.setAcceptRichText(False)
        self.tabWidget.addTab(self.MainTab, "")
        self.UserGuideTab = QWidget()
        self.UserGuideTab.setObjectName(u"UserGuideTab")
        sizePolicy.setHeightForWidth(self.UserGuideTab.sizePolicy().hasHeightForWidth())
        self.UserGuideTab.setSizePolicy(sizePolicy)
        self.guideTextEdit = QTextEdit(self.UserGuideTab)
        self.guideTextEdit.setObjectName(u"guideTextEdit")
        self.guideTextEdit.setGeometry(QRect(-2, 0, 446, 203))
        sizePolicy.setHeightForWidth(self.guideTextEdit.sizePolicy().hasHeightForWidth())
        self.guideTextEdit.setSizePolicy(sizePolicy)
        self.guideTextEdit.setFont(font2)
        self.guideTextEdit.setStyleSheet(u"")
        self.guideTextEdit.setFrameShadow(QFrame.Sunken)
        self.guideTextEdit.setReadOnly(True)
        self.tabWidget.addTab(self.UserGuideTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 451, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLogging = QMenu(self.menubar)
        self.menuLogging.setObjectName(u"menuLogging")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLogging.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuLogging.addAction(self.actionOpen_Log)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Acronyme Finder", None))
        self.actionOpen_Log.setText(QCoreApplication.translate("MainWindow", u"Open Log", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUser_Guide.setText(QCoreApplication.translate("MainWindow", u"User Guide", None))
        self.actionLoad_File.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Acronym:", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserGuideTab), QCoreApplication.translate("MainWindow", u"User Guide", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuLogging.setTitle(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

