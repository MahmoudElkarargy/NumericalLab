from sympy import *

def mainFunc(function):
    expr = sympify(function)
    x = var('x')
    sol = solve(expr, x)
    if sol==LambertW(1):
        sol=0.5671432904097
    print('\n Exact root is: %0.8f' % sol[0])
    return '%0.6f' % sol[0]