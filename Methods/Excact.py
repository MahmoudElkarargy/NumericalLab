from sympy import *
import numpy as num
import cmath

def mainFunc(function):
    expr = sympify(function)
    x = var('x')
    sol = solve(expr, x)
    if sol==LambertW(1):
        sol=0.5671432904097
    for solut in sol:
        try:
            print('\n Exact root is: %0.8f' % solut)
            return '%0.6f' % solut
        except:
            continue