# Fixed Point Iteration Method
# Importing math to use sqrt function
import math
from sympy import var
from sympy import sympify

def f(expr, value, x):
	return expr.subs(x, value)


# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(function,x0, e, N,x):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(function,x1,x)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(function,x1,x)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
        return '%0.6f' % x1
    else:
        print('\nNot Convergent.')
        return 'None'





# Main code
def mainFunc(function, N, e, x0):
    x = var('x')  # the possible variable names must be known beforehand...
    expr = sympify(function)
    # Starting Newton Raphson Method
    return fixedPointIteration(expr, x0, e, N,x)