# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 453)
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 241, 31))
        self.lineEdit.setStyleSheet("padding: 10px 0;\n"
"border: 0;\n"
"border-bottom: 1px solid #999;\n"
       "background: transparent;\n"                             
"outline: none;\n"
                                    "font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
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
        self.label_3.setGeometry(QtCore.QRect(440, 90, 141, 41))
        self.label_3.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 90, 131, 41))
        self.comboBox.setStyleSheet(
"    border: 0;\n"
"    border-bottom: 1px solid #999;\n"
"    outline: none;\n"
"    background: transparent;\n"
"    background-color: rgb(0, 0, 40);\n"    
"color: rgb(234, 255, 253);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Numerical Project"))
        self.label_2.setText(_translate("MainWindow", "Function:"))
        self.checkBox.setText(_translate("MainWindow", "Select from File"))
        self.label_3.setText(_translate("MainWindow", "Method:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Bisection"))
        self.comboBox.setItemText(1, _translate("MainWindow", "False-position"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Fixed point"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Newton-Raphson"
""))
        self.comboBox.setItemText(4, _translate("MainWindow", "Secant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
