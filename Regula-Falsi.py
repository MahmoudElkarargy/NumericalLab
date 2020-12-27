from sympy import var
from sympy import *


def func(expr, value):
    return expr.subs(x, value)

# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b, expr):
    if func(expr, a) * func(expr, b) >= 0:
        print("You have not assumed right a and b")
        return -1
    c = a
    # Initialize result
    i = MAX_ITER
    while i > 0:
        # Find the point that touches x a/xis
        old_c = c
        c = (a * func(expr, b) - b * func(expr, a)) / (func(expr, b) - func(expr, a))
        if abs(c - old_c) / c < EPSILON:
            break
        # Check if the above found point is root
        if func(expr, c) == 0:
            break
        # Decide the side to repeat the steps
        elif func(expr, c) * func(expr, a) < 0:
            b = c
        else:
            a = c
        i = i - 1

    print("The value of root is : ", '%.4f' % c)


# Driver code to test above function
# Initial values assumed
x = var('x')  # the possible variable names must be known beforehand...
function = input("Enter your function: ")
expr = sympify(function)

# Take from user assumtion of a and b.
a = int(input("Enter your assumtion for lower bond: "))
b = int(input("Enter your assumtion for upper bond-: "))
MAX_ITER = int(input("Enter number of iterations-: "))
EPSILON = float(input("Enter Epsilon-: "))

regulaFalsi(a, b, expr)

# This code is contributed by "Sharad_Bhardwaj".
