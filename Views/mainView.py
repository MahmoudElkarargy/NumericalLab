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
        self.bisectionCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.bisectionCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionCalcBtn.setObjectName("bisectionCalcBtn")
        self.bisectionShowIterBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.bisectionShowIterBtn.setGeometry(QtCore.QRect(180, 140, 161, 32))
        self.bisectionShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowIterBtn.setObjectName("bisectionShowIterBtn")
        self.bisectionShowGpBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.bisectionShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.bisectionShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowGpBtn.setObjectName("bisectionShowGpBtn")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.label_19.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_19.setObjectName("label_19")
        self.bisectionRoot = QtWidgets.QLabel(self.groupBox_2)
        self.bisectionRoot.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.bisectionRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.bisectionRoot.setText("")
        self.bisectionRoot.setObjectName("bisectionRoot")
        self.tabWidget.addTab(self.Bisection, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox.setStyleSheet("background: transparent;\n"
"")
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
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(260, 20, 121, 31))
        self.label_13.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_13.setObjectName("label_13")
        self.fixedSecondGuess = QtWidgets.QLineEdit(self.groupBox)
        self.fixedSecondGuess.setGeometry(QtCore.QRect(390, 20, 81, 21))
        self.fixedSecondGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.fixedSecondGuess.setInputMask("")
        self.fixedSecondGuess.setText("")
        self.fixedSecondGuess.setObjectName("fixedSecondGuess")
        self.fixedCalcBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.fixedCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedCalcBtn.setObjectName("fixedCalcBtn")
        self.fixedShowIterBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedShowIterBtn.setGeometry(QtCore.QRect(180, 140, 161, 32))
        self.fixedShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedShowIterBtn.setObjectName("fixedShowIterBtn")
        self.fixedShowGpBtn = QtWidgets.QPushButton(self.groupBox)
        self.fixedShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.fixedShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.fixedShowGpBtn.setObjectName("fixedShowGpBtn")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.label_14.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_14.setObjectName("label_14")
        self.fixedRoot = QtWidgets.QLabel(self.groupBox)
        self.fixedRoot.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.fixedRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.fixedRoot.setText("")
        self.fixedRoot.setObjectName("fixedRoot")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_3.setStyleSheet("background: transparent;\n"
"")
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
        self.falseCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.falseCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseCalcBtn.setObjectName("falseCalcBtn")
        self.falseShowIterBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.falseShowIterBtn.setGeometry(QtCore.QRect(180, 140, 161, 32))
        self.falseShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseShowIterBtn.setObjectName("falseShowIterBtn")
        self.falseShowGpBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.falseShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.falseShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.falseShowGpBtn.setObjectName("falseShowGpBtn")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.label_21.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_21.setObjectName("label_21")
        self.falseRoot = QtWidgets.QLabel(self.groupBox_3)
        self.falseRoot.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.falseRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.falseRoot.setText("")
        self.falseRoot.setObjectName("falseRoot")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_4.setStyleSheet("background: transparent;\n"
"")
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
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(260, 20, 121, 31))
        self.label_23.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_23.setObjectName("label_23")
        self.newtonSecondGuess = QtWidgets.QLineEdit(self.groupBox_4)
        self.newtonSecondGuess.setGeometry(QtCore.QRect(390, 20, 81, 21))
        self.newtonSecondGuess.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.newtonSecondGuess.setInputMask("")
        self.newtonSecondGuess.setText("")
        self.newtonSecondGuess.setObjectName("newtonSecondGuess")
        self.newtonCalcBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.newtonCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonCalcBtn.setObjectName("newtonCalcBtn")
        self.newtonShowIterBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonShowIterBtn.setGeometry(QtCore.QRect(180, 140, 161, 32))
        self.newtonShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonShowIterBtn.setObjectName("newtonShowIterBtn")
        self.newtonShowGpBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.newtonShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.newtonShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.newtonShowGpBtn.setObjectName("newtonShowGpBtn")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.label_25.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_25.setObjectName("label_25")
        self.newtonRoot = QtWidgets.QLabel(self.groupBox_4)
        self.newtonRoot.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.newtonRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.newtonRoot.setText("")
        self.newtonRoot.setObjectName("newtonRoot")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(-1, -1, 521, 201))
        self.groupBox_5.setStyleSheet("background: transparent;\n"
"")
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
        self.secantCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.secantCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantCalcBtn.setObjectName("secantCalcBtn")
        self.secantShowIterBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.secantShowIterBtn.setGeometry(QtCore.QRect(180, 140, 161, 32))
        self.secantShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantShowIterBtn.setObjectName("secantShowIterBtn")
        self.secantShowGpBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.secantShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.secantShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.secantShowGpBtn.setObjectName("secantShowGpBtn")
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.label_27.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_27.setObjectName("label_27")
        self.secantRoot = QtWidgets.QLabel(self.groupBox_5)
        self.secantRoot.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.secantRoot.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.secantRoot.setText("")
        self.secantRoot.setObjectName("secantRoot")
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add Methods here ....

        # Connect Bisection button to it's function
        self.bisectionCalcBtn.clicked.connect(self.BisectionCalcBtnClicked)
        self.falseCalcBtn.clicked.connect(self.RegularFalseCalcBtnClicked)
        self.secantCalcBtn.clicked.connect(self.SecantCalcBtnClicked)

    def BisectionCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        lowerBound = int(self.bisectionLowerBound.text())
        upperBound = int(self.bisectionUpperBound.text())

        result = Bisection.mainFunc(function, maxIteration, epsilon, lowerBound, upperBound)
        self.bisectionRoot.setText(str(result))

    def RegularFalseCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        lowerBound = int(self.falseLowerBound.text())
        upperBound = int(self.falseUpperBound.text())

        result = RegularFalse.mainFunc(function, maxIteration, epsilon, lowerBound, upperBound)
        self.falseRoot.setText(str(result))

    def SecantCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        firstGuess = int(self.secantFirstGuess.text())
        secondGuess = int(self.secantSecondGuess.text())

        result = Secant.mainFunc(function, maxIteration, epsilon, firstGuess, secondGuess)
        self.secantRoot.setText(str(result))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Numerical Project"))
        self.label_2.setText(_translate("MainWindow", "Function:"))
        self.checkBox.setText(_translate("MainWindow", "Select from File"))
        self.label_3.setText(_translate("MainWindow", "Method:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_16.setText(_translate("MainWindow", "Lower Bound:"))
        self.label_17.setText(_translate("MainWindow", "Upper Bound:"))
        self.bisectionCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.bisectionShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.bisectionShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_19.setText(_translate("MainWindow", "Root Result:  X = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bisection), _translate("MainWindow", "Bisection"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_12.setText(_translate("MainWindow", "First Guess:"))
        self.label_13.setText(_translate("MainWindow", "Second Guess:"))
        self.fixedCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.fixedShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.fixedShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_14.setText(_translate("MainWindow", "Root Result:  X = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Fixed point"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_18.setText(_translate("MainWindow", "Lower Bound:"))
        self.label_20.setText(_translate("MainWindow", "Upper Bound:"))
        self.falseCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.falseShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.falseShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_21.setText(_translate("MainWindow", "Root Result:  X = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "False-position"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_22.setText(_translate("MainWindow", "First Guess:"))
        self.label_23.setText(_translate("MainWindow", "Second Guess:"))
        self.newtonCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.newtonShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.newtonShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_25.setText(_translate("MainWindow", "Root Result:  X = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Newton-Raphson"))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_15.setText(_translate("MainWindow", "First Guess:"))
        self.label_24.setText(_translate("MainWindow", "Second Guess:"))
        self.secantCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.secantShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.secantShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.label_27.setText(_translate("MainWindow", "Root Result:  X = "))
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
