# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Methods.Bisection as Bisection
import Methods.RegularFalse as RegularFalse
import Methods.Secant as Secant
import Methods.FixedPoint as Fixed
import Methods.Newton as Newton
import Methods.Excact as Excact
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 453)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 40)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 391, 61))
        self.label.setStyleSheet("background: transparent;\n"
"color: rgb(166, 203, 255);\n"
"margin: 5px;\n"
"font-size: 36px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.label_2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_2.setObjectName("label_2")
        self.functionLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.functionLineEdit.setGeometry(QtCore.QRect(160, 80, 241, 41))
        self.functionLineEdit.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.functionLineEdit.setInputMask("")
        self.functionLineEdit.setText("")
        self.functionLineEdit.setObjectName("functionLineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(210, 130, 191, 21))
        self.checkBox.setStyleSheet("outline: none;\n"
"background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 141, 51))
        self.label_3.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(140, 200, 521, 231))
        self.tabWidget.setStyleSheet("border: 0;\n"
"border: 1px solid #999;\n"
"border-top: 0;\n"
"background: transparent;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"background-color: rgb(0, 0, 40);")
        self.tabWidget.setObjectName("tabWidget")
        self.Bisection = QtWidgets.QWidget()
        self.Bisection.setObjectName("Bisection")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Bisection)
        self.groupBox_2.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_2.setStyleSheet("background: transparent;\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label_16.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_16.setObjectName("label_16")
        self.bisectionLowerBound = QtWidgets.QLineEdit(self.groupBox_2)
        self.bisectionLowerBound.setGeometry(QtCore.QRect(150, 20, 81, 20))
        self.bisectionLowerBound.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.bisectionLowerBound.setInputMask("")
        self.bisectionLowerBound.setText("")
        self.bisectionLowerBound.setObjectName("bisectionLowerBound")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(260, 20, 121, 31))
        self.label_17.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_17.setObjectName("label_17")
        self.bisectionUpperBound = QtWidgets.QLineEdit(self.groupBox_2)
        self.bisectionUpperBound.setGeometry(QtCore.QRect(390, 20, 81, 21))
        self.bisectionUpperBound.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.bisectionUpperBound.setInputMask("")
        self.bisectionUpperBound.setText("")
        self.bisectionUpperBound.setObjectName("bisectionUpperBound")
        self.bisectionCalcBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.bisectionCalcBtn.setGeometry(QtCore.QRect(40, 150, 112, 32))
        self.bisectionCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionCalcBtn.setObjectName("bisectionCalcBtn")
        self.bisectionShowIterBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.bisectionShowIterBtn.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.bisectionShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowIterBtn.setObjectName("bisectionShowIterBtn")
        self.bisectionShowGpBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.bisectionShowGpBtn.setGeometry(QtCore.QRect(370, 150, 112, 32))
        self.bisectionShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowGpBtn.setObjectName("bisectionShowGpBtn")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(80, 60, 171, 31))
        self.label_19.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_19.setObjectName("label_19")
        self.bisectionRoot = QtWidgets.QLabel(self.groupBox_2)
        self.bisectionRoot.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.bisectionRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.bisectionRoot.setObjectName("bisectionRoot")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_23.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_23.setObjectName("label_23")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(260, 100, 141, 31))
        self.label_26.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_26.setObjectName("label_26")
        self.excactRootBisection = QtWidgets.QLabel(self.groupBox_2)
        self.excactRootBisection.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.excactRootBisection.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.excactRootBisection.setObjectName("excactRootBisection")
        self.etBisection = QtWidgets.QLabel(self.groupBox_2)
        self.etBisection.setGeometry(QtCore.QRect(390, 100, 101, 31))
        self.etBisection.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.etBisection.setObjectName("etBisection")
        self.tabWidget.addTab(self.Bisection, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox.setStyleSheet("background: transparent;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label_12.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_12.setObjectName("label_12")
        self.fixedFirstGuess = QtWidgets.QLineEdit(self.groupBox)
        self.fixedFirstGuess.setGeometry(QtCore.QRect(150, 20, 81, 20))
        self.fixedFirstGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.fixedFirstGuess.setInputMask("")
        self.fixedFirstGuess.setText("")
        self.fixedFirstGuess.setObjectName("fixedFirstGuess")
        self.fixedCalcBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedCalcBtn.setGeometry(QtCore.QRect(40, 150, 112, 32))
        self.fixedCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedCalcBtn.setObjectName("fixedCalcBtn")
        self.fixedShowIterBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedShowIterBtn.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.fixedShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedShowIterBtn.setObjectName("fixedShowIterBtn")
        self.fixedShowGpBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedShowGpBtn.setGeometry(QtCore.QRect(370, 150, 112, 32))
        self.fixedShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedShowGpBtn.setObjectName("fixedShowGpBtn")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(80, 60, 171, 31))
        self.label_14.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_14.setObjectName("label_14")
        self.fixedRoot = QtWidgets.QLabel(self.groupBox)
        self.fixedRoot.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.fixedRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.fixedRoot.setObjectName("fixedRoot")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_28.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_28.setObjectName("label_28")
        self.excactRootFixed = QtWidgets.QLabel(self.groupBox)
        self.excactRootFixed.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.excactRootFixed.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.excactRootFixed.setObjectName("excactRootFixed")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(260, 100, 141, 31))
        self.label_29.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_29.setObjectName("label_29")
        self.etFixed = QtWidgets.QLabel(self.groupBox)
        self.etFixed.setGeometry(QtCore.QRect(390, 100, 101, 31))
        self.etFixed.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.etFixed.setObjectName("etFixed")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_3.setStyleSheet("background: transparent;\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label_18.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_18.setObjectName("label_18")
        self.falseLowerBound = QtWidgets.QLineEdit(self.groupBox_3)
        self.falseLowerBound.setGeometry(QtCore.QRect(150, 20, 81, 20))
        self.falseLowerBound.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.falseLowerBound.setInputMask("")
        self.falseLowerBound.setText("")
        self.falseLowerBound.setObjectName("falseLowerBound")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(260, 20, 121, 31))
        self.label_20.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_20.setObjectName("label_20")
        self.falseUpperBound = QtWidgets.QLineEdit(self.groupBox_3)
        self.falseUpperBound.setGeometry(QtCore.QRect(390, 20, 81, 21))
        self.falseUpperBound.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.falseUpperBound.setInputMask("")
        self.falseUpperBound.setText("")
        self.falseUpperBound.setObjectName("falseUpperBound")
        self.falseCalcBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.falseCalcBtn.setGeometry(QtCore.QRect(40, 150, 112, 32))
        self.falseCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseCalcBtn.setObjectName("falseCalcBtn")
        self.falseShowIterBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.falseShowIterBtn.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.falseShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseShowIterBtn.setObjectName("falseShowIterBtn")
        self.falseShowGpBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.falseShowGpBtn.setGeometry(QtCore.QRect(370, 150, 112, 32))
        self.falseShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseShowGpBtn.setObjectName("falseShowGpBtn")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(80, 60, 171, 31))
        self.label_21.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_21.setObjectName("label_21")
        self.falseRoot = QtWidgets.QLabel(self.groupBox_3)
        self.falseRoot.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.falseRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.falseRoot.setObjectName("falseRoot")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_30.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_30.setObjectName("label_30")
        self.excactRootFalse = QtWidgets.QLabel(self.groupBox_3)
        self.excactRootFalse.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.excactRootFalse.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.excactRootFalse.setObjectName("excactRootFalse")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(260, 100, 141, 31))
        self.label_31.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_31.setObjectName("label_31")
        self.etFalse = QtWidgets.QLabel(self.tab_3)
        self.etFalse.setGeometry(QtCore.QRect(390, 100, 101, 31))
        self.etFalse.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.etFalse.setObjectName("etFalse")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_4.setStyleSheet("background: transparent;\n"
"")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label_22.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_22.setObjectName("label_22")
        self.newtonFirstGuess = QtWidgets.QLineEdit(self.groupBox_4)
        self.newtonFirstGuess.setGeometry(QtCore.QRect(150, 20, 81, 20))
        self.newtonFirstGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.newtonFirstGuess.setInputMask("")
        self.newtonFirstGuess.setText("")
        self.newtonFirstGuess.setObjectName("newtonFirstGuess")
        self.newtonCalcBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonCalcBtn.setGeometry(QtCore.QRect(40, 150, 112, 32))
        self.newtonCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonCalcBtn.setObjectName("newtonCalcBtn")
        self.newtonShowIterBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonShowIterBtn.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.newtonShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonShowIterBtn.setObjectName("newtonShowIterBtn")
        self.newtonShowGpBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonShowGpBtn.setGeometry(QtCore.QRect(370, 150, 112, 32))
        self.newtonShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonShowGpBtn.setObjectName("newtonShowGpBtn")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(80, 60, 191, 31))
        self.label_25.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_25.setObjectName("label_25")
        self.newtonRoot = QtWidgets.QLabel(self.groupBox_4)
        self.newtonRoot.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.newtonRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.newtonRoot.setObjectName("newtonRoot")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_32.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_32.setObjectName("label_32")
        self.excactRootNewton = QtWidgets.QLabel(self.groupBox_4)
        self.excactRootNewton.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.excactRootNewton.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.excactRootNewton.setObjectName("excactRootNewton")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(260, 100, 141, 31))
        self.label_33.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_33.setObjectName("label_33")
        self.etNewton = QtWidgets.QLabel(self.groupBox_4)
        self.etNewton.setGeometry(QtCore.QRect(390, 100, 101, 31))
        self.etNewton.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.etNewton.setObjectName("etNewton")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_5.setStyleSheet("background: transparent;\n"
"")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label_15.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_15.setObjectName("label_15")
        self.secantFirstGuess = QtWidgets.QLineEdit(self.groupBox_5)
        self.secantFirstGuess.setGeometry(QtCore.QRect(150, 20, 81, 20))
        self.secantFirstGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.secantFirstGuess.setInputMask("")
        self.secantFirstGuess.setText("")
        self.secantFirstGuess.setObjectName("secantFirstGuess")
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setGeometry(QtCore.QRect(260, 20, 121, 31))
        self.label_24.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_24.setObjectName("label_24")
        self.secantSecondGuess = QtWidgets.QLineEdit(self.groupBox_5)
        self.secantSecondGuess.setGeometry(QtCore.QRect(390, 20, 81, 21))
        self.secantSecondGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.secantSecondGuess.setInputMask("")
        self.secantSecondGuess.setText("")
        self.secantSecondGuess.setObjectName("secantSecondGuess")
        self.secantCalcBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.secantCalcBtn.setGeometry(QtCore.QRect(40, 150, 112, 32))
        self.secantCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantCalcBtn.setObjectName("secantCalcBtn")
        self.secantShowIterBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.secantShowIterBtn.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.secantShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantShowIterBtn.setObjectName("secantShowIterBtn")
        self.secantShowGpBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.secantShowGpBtn.setGeometry(QtCore.QRect(370, 150, 112, 32))
        self.secantShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantShowGpBtn.setObjectName("secantShowGpBtn")
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setGeometry(QtCore.QRect(80, 60, 171, 31))
        self.label_27.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_27.setObjectName("label_27")
        self.secantRoot = QtWidgets.QLabel(self.groupBox_5)
        self.secantRoot.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.secantRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.secantRoot.setObjectName("secantRoot")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_34.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_34.setObjectName("label_34")
        self.excactRootSecant = QtWidgets.QLabel(self.groupBox_5)
        self.excactRootSecant.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.excactRootSecant.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.excactRootSecant.setObjectName("excactRootSecant")
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        self.label_35.setGeometry(QtCore.QRect(260, 100, 141, 31))
        self.label_35.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_35.setObjectName("label_35")
        self.etSecant = QtWidgets.QLabel(self.groupBox_5)
        self.etSecant.setGeometry(QtCore.QRect(390, 100, 101, 31))
        self.etSecant.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.etSecant.setObjectName("etSecant")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(440, 90, 161, 31))
        self.label_5.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_5.setObjectName("label_5")
        self.maxIterations = QtWidgets.QSpinBox(self.centralWidget)
        self.maxIterations.setGeometry(QtCore.QRect(620, 81, 91, 41))
        self.maxIterations.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.maxIterations.setMaximum(100000000)
        self.maxIterations.setProperty("value", 50)
        self.maxIterations.setObjectName("maxIterations")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(440, 140, 161, 31))
        self.label_6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_6.setObjectName("label_6")
        self.Epsilon = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.Epsilon.setGeometry(QtCore.QRect(620, 130, 91, 41))
        self.Epsilon.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.Epsilon.setDecimals(6)
        self.Epsilon.setMaximum(1.99)
        self.Epsilon.setProperty("value", 1e-05)
        self.Epsilon.setObjectName("Epsilon")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect Bisection button to it's function
        self.bisectionCalcBtn.clicked.connect(self.BisectionCalcBtnClicked)
        self.falseCalcBtn.clicked.connect(self.RegularFalseCalcBtnClicked)
        self.secantCalcBtn.clicked.connect(self.SecantCalcBtnClicked)
        self.fixedCalcBtn.clicked.connect(self.FixedPointCalcBtnClicked)
        self.newtonCalcBtn.clicked.connect(self.NewtonCalcBtnClicked)

    def BisectionCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        lowerBound = float(self.bisectionLowerBound.text())
        upperBound = float(self.bisectionUpperBound.text())

        start_time = time.time()
        result = Bisection.mainFunc(function, maxIteration, epsilon, lowerBound, upperBound)
        self.bisectionRoot.setText(str(result))
        self.excactRootBisection.setText(str(Excact.mainFunc(function)))

        end_time = time.time()
        t2 = end_time - start_time
        self.etBisection.setText("%.6f s" % t2)

    def RegularFalseCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        lowerBound = float(self.falseLowerBound.text())
        upperBound = float(self.falseUpperBound.text())

        start_time = time.time()
        result = RegularFalse.mainFunc(function, maxIteration, epsilon, lowerBound, upperBound)
        self.falseRoot.setText(str(result))
        self.excactRootFalse.setText(str(Excact.mainFunc(function)))
        end_time = time.time()
        t2 = end_time - start_time
        self.etFalse.setText("%.6f s" % t2)

    def SecantCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        firstGuess = float(self.secantFirstGuess.text())
        secondGuess = float(self.secantSecondGuess.text())

        start_time = time.time()
        result = Secant.mainFunc(function, maxIteration, epsilon, firstGuess, secondGuess)
        self.secantRoot.setText(str(result))
        self.excactRootSecant.setText(str(Excact.mainFunc(function)))
        end_time = time.time()
        t2 = end_time - start_time
        self.etSecant.setText("%.6f s" % t2)

    def FixedPointCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Fixed Point parameters
        firstGuess = float(self.fixedFirstGuess.text())

        start_time = time.time()
        result = Fixed.mainFunc(function, maxIteration, epsilon, firstGuess)
        self.fixedRoot.setText(str(result))
        self.excactRootFixed.setText(str(Excact.mainFunc(function)))

        end_time = time.time()
        t2 = end_time - start_time
        self.etFixed.setText("%.6f s" % t2)

    def NewtonCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Fixed Point parameters
        firstGuess = float(self.newtonFirstGuess.text())

        start_time = time.time()
        result = Newton.mainFunc(function, maxIteration, epsilon, firstGuess)
        self.newtonRoot.setText(str(result))
        self.excactRootNewton.setText(str(Excact.mainFunc(function)))
        end_time = time.time()
        t2 = end_time - start_time
        self.etNewton.setText("%.6f s" % t2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Lab"))
        self.label.setText(_translate("MainWindow", "Numerical Project"))
        self.label_2.setText(_translate("MainWindow", "Function:"))
        self.checkBox.setText(_translate("MainWindow", "Select from File"))
        self.label_3.setText(_translate("MainWindow", "Method:"))
        self.label_16.setText(_translate("MainWindow", "Lower Bound:"))
        self.label_17.setText(_translate("MainWindow", "Upper Bound:"))
        self.bisectionCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.bisectionShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.bisectionShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_19.setText(_translate("MainWindow", "Root Result:  X("))
        self.bisectionRoot.setText(_translate("MainWindow", "0 ): 0"))
        self.label_23.setText(_translate("MainWindow", "Excact Root X:"))
        self.label_26.setText(_translate("MainWindow", "Execution Time:"))
        self.excactRootBisection.setText(_translate("MainWindow", "0"))
        self.etBisection.setText(_translate("MainWindow", "0 ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bisection), _translate("MainWindow", "Bisection"))
        self.label_12.setText(_translate("MainWindow", "First Guess:"))
        self.fixedCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.fixedShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.fixedShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_14.setText(_translate("MainWindow", "Root Result:  X("))
        self.fixedRoot.setText(_translate("MainWindow", "0 ): 0"))
        self.label_28.setText(_translate("MainWindow", "Excact Root X:"))
        self.excactRootFixed.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "Execution Time:"))
        self.etFixed.setText(_translate("MainWindow", "0 ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Fixed point"))
        self.label_18.setText(_translate("MainWindow", "Lower Bound:"))
        self.label_20.setText(_translate("MainWindow", "Upper Bound:"))
        self.falseCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.falseShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.falseShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_21.setText(_translate("MainWindow", "Root Result:  X("))
        self.falseRoot.setText(_translate("MainWindow", "0 ): 0"))
        self.label_30.setText(_translate("MainWindow", "Excact Root X:"))
        self.excactRootFalse.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "Execution Time:"))
        self.etFalse.setText(_translate("MainWindow", "0 ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "False-position"))
        self.label_22.setText(_translate("MainWindow", "First Guess:"))
        self.newtonCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.newtonShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.newtonShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_25.setText(_translate("MainWindow", "Root Result:  X("))
        self.newtonRoot.setText(_translate("MainWindow", "0 ): 0"))
        self.label_32.setText(_translate("MainWindow", "Excact Root X:"))
        self.excactRootNewton.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "Execution Time:"))
        self.etNewton.setText(_translate("MainWindow", "0 ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Newton-Raphson"))
        self.label_15.setText(_translate("MainWindow", "First Guess:"))
        self.label_24.setText(_translate("MainWindow", "Second Guess:"))
        self.secantCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.secantShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.secantShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_27.setText(_translate("MainWindow", "Root Result:  X("))
        self.secantRoot.setText(_translate("MainWindow", "0 ): 0"))
        self.label_34.setText(_translate("MainWindow", "Excact Root X:"))
        self.excactRootSecant.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "Execution Time:"))
        self.etSecant.setText(_translate("MainWindow", "0 ms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Secant"))
        self.label_5.setText(_translate("MainWindow", "Max Iteration:"))
        self.label_6.setText(_translate("MainWindow", "Epsilon:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
