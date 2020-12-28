from sympy import *
import sympy as sp


def func(expr, value):
    x = var('x')
    return expr.subs(x, value)


def derivFunc(expr, value):
    x = var('x')
    expr = diff(expr)
    return expr.subs(x, value)


# Function to find the root
def newtonRaphson(xi, expr, Epsilon):
    h = func(expr, xi) / derivFunc(expr, xi)

    while abs(h) >= Epsilon:
        h = func(expr, xi) / derivFunc(expr, xi)

        # x(i+1) = x(i) - f(x) / f'(x)
        xi = xi - h

    print("The value of the root is : ",
          "%.4f" % xi)


def mainFunc():
    function = input("Enter your function: ")
    expr = sympify(function)
    xi = int(input("Enter initial value : "))
    Epsilon = float(input("Enter Epsilon: "))
    newtonRaphson(xi, expr, Epsilon)


