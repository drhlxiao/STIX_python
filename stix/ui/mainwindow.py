# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1376, 1044)
        MainWindow.setMaximumSize(QtCore.QSize(323232, 323232))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/images/app.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.packetTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packetTab.sizePolicy().hasHeightForWidth())
        self.packetTab.setSizePolicy(sizePolicy)
        self.packetTab.setObjectName("packetTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.packetTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.packetTab)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.packetTreeWidget = QtWidgets.QTreeWidget(self.splitter_2)
        self.packetTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.packetTreeWidget.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.packetTreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.packetTreeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.packetTreeWidget.setWordWrap(False)
        self.packetTreeWidget.setObjectName("packetTreeWidget")
        self.packetTreeWidget.headerItem().setText(0, "Timestamp")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.paramTreeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.paramTreeWidget.setAutoExpandDelay(-1)
        self.paramTreeWidget.setUniformRowHeights(True)
        self.paramTreeWidget.setObjectName("paramTreeWidget")
        self.paramTreeWidget.headerItem().setText(0, "Name")
        self.paramTreeWidget.header().setCascadingSectionResizes(False)
        self.paramTreeWidget.header().setDefaultSectionSize(170)
        self.paramTreeWidget.header().setHighlightSections(True)
        self.horizontalLayout_2.addWidget(self.splitter_3)
        self.tabWidget.addTab(self.packetTab, "")
        self.plotTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotTab.sizePolicy().hasHeightForWidth())
        self.plotTab.setSizePolicy(sizePolicy)
        self.plotTab.setObjectName("plotTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.plotTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.xaxisComboBox = QtWidgets.QComboBox(self.plotTab)
        self.xaxisComboBox.setObjectName("xaxisComboBox")
        self.xaxisComboBox.addItem("")
        self.xaxisComboBox.addItem("")
        self.xaxisComboBox.addItem("")
        self.gridLayout.addWidget(self.xaxisComboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.plotTab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.styleEdit = QtWidgets.QLineEdit(self.plotTab)
        self.styleEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.styleEdit.setObjectName("styleEdit")
        self.gridLayout.addWidget(self.styleEdit, 0, 10, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(25, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 11, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.plotTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.paramNameEdit = QtWidgets.QLineEdit(self.plotTab)
        self.paramNameEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.paramNameEdit.setObjectName("paramNameEdit")
        self.gridLayout.addWidget(self.paramNameEdit, 0, 5, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.plotTab)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 6, 1, 1)
        self.descLabel = QtWidgets.QLabel(self.plotTab)
        self.descLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.descLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.descLabel.setText("")
        self.descLabel.setObjectName("descLabel")
        self.gridLayout.addWidget(self.descLabel, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.plotTab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 9, 1, 1)
        self.plotButton = QtWidgets.QPushButton(self.plotTab)
        self.plotButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.plotButton.setObjectName("plotButton")
        self.gridLayout.addWidget(self.plotButton, 0, 13, 1, 1)
        self.savePlotButton = QtWidgets.QPushButton(self.plotTab)
        self.savePlotButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.savePlotButton.setObjectName("savePlotButton")
        self.gridLayout.addWidget(self.savePlotButton, 0, 15, 1, 1)
        self.dataTypeComboBox = QtWidgets.QComboBox(self.plotTab)
        self.dataTypeComboBox.setObjectName("dataTypeComboBox")
        self.dataTypeComboBox.addItem("")
        self.dataTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.dataTypeComboBox, 0, 8, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.plotTab)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout.addWidget(self.exportButton, 0, 16, 1, 1)
        self.autoUpdateButton = QtWidgets.QPushButton(self.plotTab)
        self.autoUpdateButton.setObjectName("autoUpdateButton")
        self.gridLayout.addWidget(self.autoUpdateButton, 0, 14, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.plotTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.spidLineEdit = QtWidgets.QLineEdit(self.plotTab)
        self.spidLineEdit.setObjectName("spidLineEdit")
        self.gridLayout.addWidget(self.spidLineEdit, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.plotTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1376, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menu_Tools = QtWidgets.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statusListWidget = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.statusListWidget.setObjectName("statusListWidget")
        self.horizontalLayout_3.addWidget(self.statusListWidget)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setObjectName("actionNext")
        self.actionSetIDB = QtWidgets.QAction(MainWindow)
        self.actionSetIDB.setObjectName("actionSetIDB")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/images/graph.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon1)
        self.actionPlot.setObjectName("actionPlot")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/images/paste.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon2)
        self.actionPaste.setObjectName("actionPaste")
        self.actionLoadMongodb = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/images/mongodb.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadMongodb.setIcon(icon3)
        self.actionLoadMongodb.setObjectName("actionLoadMongodb")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/images/copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon4)
        self.actionCopy.setObjectName("actionCopy")
        self.actionConnectTSC = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/images/link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnectTSC.setIcon(icon5)
        self.actionConnectTSC.setObjectName("actionConnectTSC")
        self.actionPacketFilter = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/images/filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPacketFilter.setIcon(icon6)
        self.actionPacketFilter.setObjectName("actionPacketFilter")
        self.actionPlugins = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/images/plugin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlugins.setIcon(icon7)
        self.actionPlugins.setObjectName("actionPlugins")
        self.actionOnlineHelp = QtWidgets.QAction(MainWindow)
        self.actionOnlineHelp.setObjectName("actionOnlineHelp")
        self.actionViewBinary = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/images/binary.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewBinary.setIcon(icon8)
        self.actionViewBinary.setObjectName("actionViewBinary")
        self.actionPacketServer = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/images/socket.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPacketServer.setIcon(icon9)
        self.actionPacketServer.setObjectName("actionPacketServer")
        self.actionPythonConsole = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/images/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPythonConsole.setIcon(icon10)
        self.actionPythonConsole.setObjectName("actionPythonConsole")
        self.actionTimestampConvertor = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/images/datetime.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTimestampConvertor.setIcon(icon11)
        self.actionTimestampConvertor.setObjectName("actionTimestampConvertor")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionOnlineHelp)
        self.menu_Help.addAction(self.actionAbout)
        self.menuSetting.addAction(self.actionSetIDB)
        self.menu_Tools.addAction(self.actionPlot)
        self.menu_Tools.addAction(self.actionLoadMongodb)
        self.menu_Tools.addAction(self.actionConnectTSC)
        self.menu_Tools.addAction(self.actionPacketFilter)
        self.menu_Tools.addAction(self.actionPlugins)
        self.menu_Tools.addAction(self.actionViewBinary)
        self.menu_Tools.addAction(self.actionTimestampConvertor)
        self.menuAction.addAction(self.actionPrevious)
        self.menuAction.addAction(self.actionNext)
        self.menuAction.addAction(self.actionLog)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCopy)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlugins)
        self.toolBar.addAction(self.actionPacketFilter)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTimestampConvertor)
        self.toolBar.addAction(self.actionLoadMongodb)
        self.toolBar.addAction(self.actionConnectTSC)
        self.toolBar.addAction(self.actionViewBinary)
        self.toolBar.addAction(self.actionPacketServer)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STIX data parser and viewer"))
        self.packetTreeWidget.headerItem().setText(1, _translate("MainWindow", "Description"))
        self.paramTreeWidget.headerItem().setText(1, _translate("MainWindow", "Description"))
        self.paramTreeWidget.headerItem().setText(2, _translate("MainWindow", "Raw"))
        self.paramTreeWidget.headerItem().setText(3, _translate("MainWindow", "Eng. /Decomp. Value"))
        self.paramTreeWidget.headerItem().setText(4, _translate("MainWindow", "Unit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packetTab), _translate("MainWindow", "Packets"))
        self.plotTab.setToolTip(_translate("MainWindow", "plot parameters\n"
""))
        self.xaxisComboBox.setItemText(0, _translate("MainWindow", "Param. repeat # as X"))
        self.xaxisComboBox.setItemText(1, _translate("MainWindow", "Timestamp - T0 as X"))
        self.xaxisComboBox.setItemText(2, _translate("MainWindow", "Histogram"))
        self.label.setText(_translate("MainWindow", "Param.:"))
        self.styleEdit.setText(_translate("MainWindow", "-"))
        self.label_4.setText(_translate("MainWindow", "Type:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "In the same packet"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Of all loaded packets"))
        self.label_3.setText(_translate("MainWindow", "Curve Style:"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.savePlotButton.setText(_translate("MainWindow", "Save"))
        self.dataTypeComboBox.setItemText(0, _translate("MainWindow", "Raw values"))
        self.dataTypeComboBox.setItemText(1, _translate("MainWindow", "Eng./Decompr. values"))
        self.exportButton.setText(_translate("MainWindow", "Export data"))
        self.autoUpdateButton.setText(_translate("MainWindow", "Start Auto Update"))
        self.label_2.setText(_translate("MainWindow", "SPID:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plotTab), _translate("MainWindow", "Plot"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menuSetting.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Tools.setTitle(_translate("MainWindow", "&Tools"))
        self.menuAction.setTitle(_translate("MainWindow", "&View"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Log"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPrevious.setText(_translate("MainWindow", "Previous"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionSetIDB.setText(_translate("MainWindow", "Set &IDB"))
        self.actionSave.setText(_translate("MainWindow", "Sa&ve"))
        self.actionLog.setText(_translate("MainWindow", "Show Log"))
        self.actionPlot.setText(_translate("MainWindow", "&Plot"))
        self.actionPaste.setText(_translate("MainWindow", "P&aste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Read raw data from the clipboard"))
        self.actionLoadMongodb.setText(_translate("MainWindow", "Connect MonogoDB"))
        self.actionCopy.setText(_translate("MainWindow", "&Copy"))
        self.actionConnectTSC.setText(_translate("MainWindow", "Connect to TSC"))
        self.actionPacketFilter.setText(_translate("MainWindow", "Packet Filter"))
        self.actionPlugins.setText(_translate("MainWindow", "Plugin manager"))
        self.actionOnlineHelp.setText(_translate("MainWindow", "Online help"))
        self.actionViewBinary.setText(_translate("MainWindow", "Packet binary data"))
        self.actionViewBinary.setIconText(_translate("MainWindow", "Binary data viewer"))
        self.actionViewBinary.setToolTip(_translate("MainWindow", "Binary data viewer"))
        self.actionPacketServer.setText(_translate("MainWindow", "Packet server"))
        self.actionPythonConsole.setText(_translate("MainWindow", "Python console"))
        self.actionTimestampConvertor.setText(_translate("MainWindow", "Timestamp convertor"))
from stix.ui import mainwindow_rc5
