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
        self.label_2.setGeometry(QtCore.QRect(30, 100, 111, 21))
        self.label_2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_2.setObjectName("label_2")
        self.functionLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.functionLineEdit.setGeometry(QtCore.QRect(160, 90, 241, 31))
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
        self.checkBox.setStyleSheet("padding: 10px 0;\n"
"outline: none;\n"
"background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 141, 41))
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
        self.label_4 = QtWidgets.QLabel(self.Bisection)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 121, 21))
        self.label_4.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.bisectionLowerBound = QtWidgets.QLineEdit(self.Bisection)
        self.bisectionLowerBound.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.bisectionLowerBound.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.bisectionLowerBound.setInputMask("")
        self.bisectionLowerBound.setObjectName("bisectionLowerBound")
        self.label_7 = QtWidgets.QLabel(self.Bisection)
        self.label_7.setGeometry(QtCore.QRect(260, 20, 121, 21))
        self.label_7.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_7.setObjectName("label_7")
        self.bisectionUpperBound = QtWidgets.QLineEdit(self.Bisection)
        self.bisectionUpperBound.setGeometry(QtCore.QRect(390, 20, 81, 16))
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
        self.label_8 = QtWidgets.QLabel(self.Bisection)
        self.label_8.setGeometry(QtCore.QRect(120, 70, 191, 21))
        self.label_8.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"border: none;")
        self.label_8.setObjectName("label_8")
        self.bisectionCalcBtn = QtWidgets.QPushButton(self.Bisection)
        self.bisectionCalcBtn.setGeometry(QtCore.QRect(40, 140, 112, 32))
        self.bisectionCalcBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionCalcBtn.setObjectName("bisectionCalcBtn")
        self.bisectionShowIterBtn = QtWidgets.QPushButton(self.Bisection)
        self.bisectionShowIterBtn.setGeometry(QtCore.QRect(181, 140, 161, 32))
        self.bisectionShowIterBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowIterBtn.setObjectName("bisectionShowIterBtn")
        self.bisectionShowGpBtn = QtWidgets.QPushButton(self.Bisection)
        self.bisectionShowGpBtn.setGeometry(QtCore.QRect(370, 140, 112, 32))
        self.bisectionShowGpBtn.setStyleSheet("border-radius: 50px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);")
        self.bisectionShowGpBtn.setObjectName("bisectionShowGpBtn")
        self.bisectionRoot = QtWidgets.QLabel(self.Bisection)
        self.bisectionRoot.setGeometry(QtCore.QRect(300, 70, 141, 21))
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
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(440, 100, 161, 21))
        self.label_5.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_5.setObjectName("label_5")
        self.maxIterations = QtWidgets.QSpinBox(self.centralWidget)
        self.maxIterations.setGeometry(QtCore.QRect(620, 91, 91, 31))
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
        self.label_6.setGeometry(QtCore.QRect(440, 140, 161, 21))
        self.label_6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_6.setObjectName("label_6")
        self.Epsilon = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.Epsilon.setGeometry(QtCore.QRect(620, 130, 91, 31))
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
        self.bisectionCalcBtn.clicked.connect(self.bisectionCalcBtnClicked)

    def bisectionCalcBtnClicked(self):
        # Same for all methods
        function = self.functionLineEdit.text()
        maxIteration = int(self.maxIterations.text())
        epsilon = float(self.Epsilon.text())
        # Bisection parameters
        lowerBound = int(self.bisectionLowerBound.text())
        upperBound = int(self.bisectionUpperBound.text())

        # print(function)
        # print(maxIteration)
        # print(epsilon)
        # print(lowerBound)
        # print(upperBound)

        result = Bisection.mainFunc(function, maxIteration, epsilon, lowerBound, upperBound)
        self.bisectionRoot.setText(str(result))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical lab"))
        self.label.setText(_translate("MainWindow", "Numerical Project"))
        self.label_2.setText(_translate("MainWindow", "Function:"))
        self.checkBox.setText(_translate("MainWindow", "Select from File"))
        self.label_3.setText(_translate("MainWindow", "Method:"))
        self.label_4.setText(_translate("MainWindow", "lower bound:"))
        self.label_7.setText(_translate("MainWindow", "upper bound:"))
        self.label_8.setText(_translate("MainWindow", "Root Result:  X = "))
        self.bisectionCalcBtn.setText(_translate("MainWindow", "Calculate"))
        self.bisectionShowIterBtn.setText(_translate("MainWindow", "Show Iterations"))
        self.bisectionShowGpBtn.setText(_translate("MainWindow", "Show graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bisection), _translate("MainWindow", "Bisection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Fixed point"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "False-position"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Newton-Raphson"))
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
