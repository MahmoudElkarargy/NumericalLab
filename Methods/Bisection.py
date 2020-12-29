
# Python program for implementation
# of Bisection Method for
# solving equations

# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2 + 2

from sympy import var
from sympy import sympify
from sympy.solvers import solve
from sympy import *
import time

def func(expr, value, x):
	return expr.subs(x, value)

iterationStr = "*** BISECTION METHOD ITERATIONS ***\n"

# Prints root of func(x)
# with error of EPSILON
def bisection(a, b, expr, maxIteration, Epsilon, x):

    if (func(expr,a, x) * func(expr,b, x) >= 0):
        print("You have not assumed right a and b\n")
        return
    c = a
    step = 1
    start_time = time.time()
    while ((b-a) >= Epsilon and step < maxIteration):
    	# Find middle point
        print('Iteration(%d): X(lower) | f(X-lower) | X(upper) | f(X-upper) | X(mid) | f(X-mid)' % step)
        print("\t\t\t %.6f \t %.6f \t  %.6f \t %.6f \t %.6f \t %.6f \n" % (
        a, func(expr, a, x), b, func(expr, b, x), c, func(expr, c, x)))

        c = (a+b)/2

		# Check if middle point is root
        if (func(expr,c, x) == 0.0):
	        break

		# Decide the side to repeat the steps
        if (func(expr,c, x)*func(expr,a, x) < 0):
            b = c
        else:
            a = c
        step +=1

        # iterationStr.append(str('Iteration(%d): X(lower) | f(X-lower) | X(upper) | f(X-upper) | X(mid) | f(X-mid)' % step))
        # iterationStr.append(str("\t\t\t %.6f \t %.6f \t  %.6f \t %.6f \t %.6f \t %.6f \n"%(a, func(expr,a,x), b, func(expr,b,x), c, func(expr,c,x))))

    finalIteration = step
    print(finalIteration)
    # print(iterationStr)
    end_time = time.time()
    t2 = end_time - start_time
    print("execution time for Bisection=", "%.6f" " sec" % t2)
    return "%d ): %.6f"%(finalIteration,c)

# Main code
def mainFunc(function, maxIteration, epsilon, a, b):
     # the possible variable names must be known beforehand...
    expr = sympify(function)
    print("hi1")
    x = var('x')
    print("hi2")
    sol = solve(expr, x)
    print("hi3")
    print(sol)
    if sol==LambertW(1):
        sol=0.5671432904097
    print('\n Exact root is: %0.8f' % sol[0])
    return bisection(a, b, expr, maxIteration, epsilon, x)

