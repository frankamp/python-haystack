# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Feb 21 20:08:27 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1191, 639)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Haystack Memory analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(False)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setEnabled(False)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setTitle(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSearch.setObjectName(_fromUtf8("menuSearch"))
        self.menu_tools = QtGui.QMenu(self.menubar)
        self.menu_tools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tools.setObjectName(_fromUtf8("menu_tools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menu_file_open = QtGui.QAction(MainWindow)
        self.menu_file_open.setText(QtGui.QApplication.translate("MainWindow", "Open dumpfile", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open a nenory dump file", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open a memory dump file", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setObjectName(_fromUtf8("menu_file_open"))
        self.menu_file_exit = QtGui.QAction(MainWindow)
        self.menu_file_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setObjectName(_fromUtf8("menu_file_exit"))
        self.actionSearch_Structure = QtGui.QAction(MainWindow)
        self.actionSearch_Structure.setText(QtGui.QApplication.translate("MainWindow", "Search Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch_Structure.setObjectName(_fromUtf8("actionSearch_Structure"))
        self.menu_search_value = QtGui.QAction(MainWindow)
        self.menu_search_value.setText(QtGui.QApplication.translate("MainWindow", "Search value", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_value.setObjectName(_fromUtf8("menu_search_value"))
        self.menu_search_structure = QtGui.QAction(MainWindow)
        self.menu_search_structure.setText(QtGui.QApplication.translate("MainWindow", "Search Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_structure.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_structure.setObjectName(_fromUtf8("menu_search_structure"))
        self.menu_file_close = QtGui.QAction(MainWindow)
        self.menu_file_close.setText(QtGui.QApplication.translate("MainWindow", "Close tab", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_close.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_close.setObjectName(_fromUtf8("menu_file_close"))
        self.menu_tools_addmodule = QtGui.QAction(MainWindow)
        self.menu_tools_addmodule.setText(QtGui.QApplication.translate("MainWindow", "Add haystack module", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tools_addmodule.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tools_addmodule.setObjectName(_fromUtf8("menu_tools_addmodule"))
        self.menu_file_open_process = QtGui.QAction(MainWindow)
        self.menu_file_open_process.setText(QtGui.QApplication.translate("MainWindow", "Open process", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open_process.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open a live process", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open_process.setObjectName(_fromUtf8("menu_file_open_process"))
        self.menu_tools_list_structures = QtGui.QAction(MainWindow)
        self.menu_tools_list_structures.setText(QtGui.QApplication.translate("MainWindow", "List structures allocations", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tools_list_structures.setObjectName(_fromUtf8("menu_tools_list_structures"))
        self.menuFile.addAction(self.menu_file_open)
        self.menuFile.addAction(self.menu_file_open_process)
        self.menuFile.addAction(self.menu_file_close)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_file_exit)
        self.menuSearch.addAction(self.menu_search_structure)
        self.menuSearch.addAction(self.menu_search_value)
        self.menu_tools.addAction(self.menu_tools_addmodule)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.menu_file_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

