
from sympy import *
import time


# Defining Function
def f(y, Function):
    x = var('x')
    return Function.subs(x, y)


# Implementing Secant Method

def secant(x0, x1, e, N, Function):
    print('\n\n*** SECANT METHOD IMPLEMENTATION *')
    step = 1
    condition = True
    start_time = time.time()
    while condition:
        if f(x0, Function) == f(x1, Function):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0, Function) / (f(x1, Function) - f(x0, Function))
        fx=f(x2,Function)
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2, Function)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2, Function)) > e
    end_time = time.time()
    t4= end_time - start_time
    print("execution time for Secant=", "%.6f" " sec" % t4)
    return "%d ): %.6f" % (step, x2)

def mainFunc(expr, N, e, x0, x1):

    Function = sympify(expr)
    x = var('x')
    sol = solve(Function, x)
    if sol==LambertW(1):
        sol=0.5671432904097
    print('\n Exact root is: %0.8f' % sol[0])
    # Starting Secant Method
    return secant(x0, x1, e, N, Function)