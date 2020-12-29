# Fixed Point Iteration Method
# Importing math to use sqrt function
from sympy import *
import time

def f(expr, value, x):
	return expr.subs(x, value)


def derivFunc(expr, value):
    x = var('x')
    expr = diff(expr)
    return expr.subs(x, value)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(function,x0, e, N,x):

    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    #start_time = time.time()
    condition = True
    while condition:
        x1 = derivFunc(function,x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(function,x1,x)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(function,x1,x)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
        return "%d ): %.6f" % (step, x1)
    else:
        print('\nNot Convergent.')
        return 'None'

 #end_time = time.time()
 #t5 = end_time - start_time
 #print("execution time for FixedPoint=", "%.6f" " sec" % t5)







# Main code
def mainFunc(function, N, e, x0):
    x = var('x')  # the possible variable names must be known beforehand...
    expr = sympify(function)

    sol = solve(Function, x)
    if sol==LambertW(1):
        sol=0.5671432904097
    print('\n Exact root is: %0.8f' % sol[0])
    # Starting Newton Raphson Method
    return fixedPointIteration(expr, x0, e, N,x)