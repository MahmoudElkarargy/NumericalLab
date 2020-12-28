from sympy import var
from sympy import sympify


def func(expr, value, x):
    return expr.subs(x, value)


MAX_ITER = 1000000
EPSILON = 0.00001


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2

# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b, expr, x,MAX_ITER, EPSILON):
    if func(expr, a, x) * func(expr, b, x) >= 0:
        print("You have not assumed right a and b")
        return -1
    c = a
    # Initialize result
    i = MAX_ITER
    old_c = int();
    while i > 0:
        # Find the point that touches x a/xis
        c = (a * func(expr, b, x) - b * func(expr, a, x)) / (func(expr, b, x) - func(expr, a, x))
        if abs(abs(c - old_c) / c) < EPSILON:
            break
        # Check if the above found point is root
        if func(expr, c, x) == 0:
            break
        # Decide the side to repeat the steps
        elif func(expr, c, x) * func(expr, a, x) < 0:
            b = c
        else:
            a = c
        i = i - 1
        old_c = c
    return '%.4f' % c

def mainFunc(function, maxIteration, epsilon, a, b):
    x = var('x')  # the possible variable names must be known beforehand...
    expr = sympify(function)
    print("bsmallah")
    return regulaFalsi(a, b, expr, x, maxIteration, epsilon)

