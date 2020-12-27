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
def regulaFalsi(a, b, expr, MAX_ITER, EPSILON, x):
    if func(expr, a, x) * func(expr, b, x) >= 0:
        print("You have not assumed right a and b")
        return -1
    c = a
    # Initialize result
    i = MAX_ITER
    while i > 0:
        # Find the point that touches x a/xis
        old_c = c
        c = (a * func(expr, b, x) - b * func(expr, a, x)) / (func(expr, b, x) - func(expr, a, x))
        if abs(c - old_c) / c < EPSILON:
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

    print("The value of root is : ", '%.4f' % c)

def mainFunc():
    # Driver code to test above function
    # Initial values assumed
    x = var('x')  # the possible variable names must be known beforehand...
    function = input("Enter your function: ")
    expr = sympify(function)
    print
    # Take from user assumtion of a and b.
    a = int(input("Enter your assumtion for lower bond: "))
    b = int(input("Enter your assumtion for upper bond: "))
    MAX_ITER = int(input("Enter number of iterations: "))
    EPSILON = float(input("Enter Epsilon-: "))

    regulaFalsi(a, b, expr, MAX_ITER, EPSILON, x)

