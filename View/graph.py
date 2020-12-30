from math import exp


from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import numpy as np
import Methods.Bisection as bisection
from sympy import *
import os.path


class Ui_SecondWindow(object):

    function = ""
    maxIteration = 0
    epsilon = 0
    a = 0
    b = 0
    def __init__(self, function,maxIteration, epsilon, a, b):
        print(function)
        self.function = function
        self.maxIteration = maxIteration
        self.epsilon = epsilon
        self.a = a
        self.b = b

    def setupUi(self, MainWindow):
        # self.function = input("Enter your function")
        bisection.mainFunc(self.function, self.maxIteration, self.epsilon, self.a, self.b)
        # super(Ui_MainWindow, self).__init__(*args, **kwargs)

        MainWindow.graphWidget = pg.PlotWidget()
        MainWindow.setCentralWidget(MainWindow.graphWidget)
        # random data
        start = self.a-1
        stop = self.b+1
        step = 0.001

        float_range_array = np.arange(start, stop, step)
        float_range_array = np.array(float_range_array, dtype=float)
        self.float_range_list = list(float_range_array)
        #print(self.float_range_list)
        # functions will be added here
        self.expr = sympify(self.function)
        x = var('x')
        scale = int((stop-start)//step)+1
        self.data = np.zeros((scale,), dtype=float)
        print(len(self.float_range_list))
        i = 0
        while i < len(self.float_range_list):
          # print(self.float_range_list[i])
            result = self.expr.subs(x, self.float_range_list[i])
            self.data[i] = result
            #print(self.data[i])
            i = i+1
        #self.data = [self.expr.subs(x, value) for value in self.float_range_list]
        MainWindow.graphWidget.showGrid(x=True, y=True)
        MainWindow.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))


        self.file = open("../View/values.txt", "r")

        if os.path.isfile('../View/values.txt'):
            print("File exist")
        else:
            print("File not exist")


        self.input = [float(x) for x in next(self.file).split()]
        print(self.input)
        MainWindow.graphWidget.plot(self.float_range_list, self.data, pen=pen)
        self.a_values = [self.input[0],  self.input[2]]
        self.b_values = [self.input[1], self.input[3]]
        pen2 = pg.mkPen(color=(0, 0, 255), width=3)
        self.data_line = MainWindow.graphWidget.plot(self.a_values, self.b_values, pen=pen2)

       # self.graphWidget.plot(self.tuples, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()


    def update_plot_data(self):
        next_line = next(self.file)
        if(next_line != None):
            self.input = [float(x) for x in next_line.split()]
            self.a_values = self.a_values[2:]  # Remove the first y element.
            self.a_values.append(self.input[0])
            self.a_values.append(self.input[2])  # Add a new value 1 higher than the last.
            self.b_values = self.b_values[2:]  # Remove the first
            self.b_values.append(self.input[1])
            self.b_values.append(self.input[3])  # Add a new random value.
            self.data_line.setData(self.a_values, self.b_values)  # Update the data.
        else:
            pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(graph)
    graph.show()
    sys.exit(app.exec_())
