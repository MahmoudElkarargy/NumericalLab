# Fixed Point Iteration Method
# Importing math to use sqrt function
import math
from sympy import *

def func(expr, value, x):
	return expr.subs(x, value)


# Re-writing f(x)=0 to x = g(x)
def funcg(expr, value, x):
    return expr.subs(x, value)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(expr, gx, x0, e, N, x):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = funcg(gx, x0, x)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, func(expr, x1, x)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(func(expr, x1, x)) > e

    if flag == 1:
        # print('\nRequired root is: %0.8f' % x1)
        return "%d ): %.6f" % (step, x1)
    else:
        print('\nNot Convergent.')



# Main code
def mainFunc(function, g_x, N, e, x0):
    x = var('x')  # the possible variable names must be known beforehand...
    expr = sympify(function)
    g_x = sympify(g_x)
    return fixedPointIteration(expr, g_x,x0, e, N,x)