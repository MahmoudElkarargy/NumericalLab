from sympy import *
import sympy as sp
import time


def func(expr, value):
    x = var('x')
    return expr.subs(x, value)


def derivFunc(expr, value):
    x = var('x')
    expr = diff(expr)
    return expr.subs(x, value)


# Function to find the root
def newtonRaphson(xi, expr, epsilon, maxIteration):


    h = func(expr, xi) / derivFunc(expr, xi)

    step = 1
    start_time = time.time()
    while abs(h) >= epsilon and step < maxIteration:
        print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xi, func(expr, xi)))
        h = func(expr, xi) / derivFunc(expr, xi)

        # x(i+1) = x(i) - f(x) / f'(x)
        xi = xi - h
        step += 1

    print("The value of the root is : ",
          "%.4f" % xi)
    end_time = time.time()
    t1 = end_time - start_time
    print("execution time for NewtonRaphson=", "%.6f" " sec" % t1)

    return "%d ): %.6f" % (step, xi)


def mainFunc(function, maxIteration, epsilon, xi):
    expr = sympify(function)
    return newtonRaphson(xi, expr, epsilon, maxIteration)


