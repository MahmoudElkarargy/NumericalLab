# Fixed Point Iteration Method
# Importing math to use sqrt function
from sympy import *
import time

def f(expr, value):
    x = var('x')
    return expr.subs(x, value)


def derivFunc(expr, value):
    x = var('x')
    expr = diff(expr)
    return expr.subs(x, value)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(function, g_x, x0, e, N,x):

    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    start_time = time.time()
    x0 = 0
    x1 = 0
    i =0
    while i<N:
        x1 = f(g_x,x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(function,x1)))
      #  print(abs((x0-x1)/x1 ))
        if abs((x0-x1)/x1 )< e:
            break
        x0 = x1
        i = i + 1

    print('\nRequired root is: %0.8f' % x1)
    return "%d ): %.6f" % (i, x1)

    end_time = time.time()
    t5 = end_time - start_time
    print("execution time for FixedPoint=", "%.6f" " sec" % t5)







# Main code
def mainFunc(function, g_x, N, e, x0):
    x = var('x')  # the possible variable names must be known beforehand...
    expr = sympify(function)
    g_x = sympify(g_x)
    # Starting Newton Raphson Method
    return fixedPointIteration(expr, g_x,x0, e, N,x)