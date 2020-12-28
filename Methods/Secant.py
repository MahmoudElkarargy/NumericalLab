
from sympy import *


# Defining Function
def f(y, Function):
    x = var('x')
    return Function.subs(x, y)


# Implementing Secant Method

def secant(x0, x1, e, N, Function):
    print('\n\n*** SECANT METHOD IMPLEMENTATION *')
    step = 1
    condition = True
    while condition:
        if f(x0, Function) == f(x1, Function):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0, Function) / (f(x1, Function) - f(x0, Function))
        fx2=f(x2,Function)
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2,fx2))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        if abs(fx2) < e :
            break

    return '%0.6f' % x2

def mainFunc(expr, N, e, x0, x1):

    Function = sympify(expr)
    # Starting Secant Method
    return secant(x0, x1, e, N, Function)