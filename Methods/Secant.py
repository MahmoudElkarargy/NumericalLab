
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
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2, Function)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2, Function)) > e
    print('\n Required root is: %0.8f' % x2)

def mainFunc():

    x0 = float(input('Enter First Guess: '))
    x1 = float(input('Enter Second Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))
    expr = input('please enter equation: ')
    Function = sympify(expr)

    # Starting Secant Method
    secant(x0, x1, e, N, Function)