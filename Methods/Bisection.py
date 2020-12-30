
# Python program for implementation
# of Bisection Method for
# solving equations

from sympy import *
import os.path

def func(expr, value, x):
	return expr.subs(x, value)


# Prints root of func(x)
# with error of EPSILON
def bisection(a, b, expr, maxIteration, Epsilon, x):
    print("In bisectiooon")
    file = open("../View/values.txt", "w")
    if os.path.isfile('../Viewss/values.txt'):
        print("File exist")
    else:
        print("File not exist")

    if (func(expr,a, x) * func(expr,b, x) >= 0):
        print("You have not assumed right a and b\n")
        return
    c = a
    step = 1
    while (step < maxIteration):
    	# Find middle point
        print('Iteration(%d): X(lower) | f(X-lower) | X(upper) | f(X-upper) | X(mid) | f(X-mid)' % step)
        print("\t\t\t %.6f \t %.6f \t  %.6f \t %.6f \t %.6f \t %.6f \n" % (
        a, func(expr, a, x), b, func(expr, b, x), c, func(expr, c, x)))

        file.write("%.6f %.6f %.6f %.6f %.6f %.6f \n" % (
            a, func(expr, a, x), b, func(expr, b, x), c, func(expr, c, x)))

        c_old=c
        c = (a+b)/2
        if(abs((c-c_old)/c)<Epsilon):
            break

		# Check if middle point is root
        if (func(expr,c, x) == 0.0):
	        break

		# Decide the side to repeat the steps
        if (func(expr,c, x)*func(expr,a, x) < 0):
            b = c
        else:
            a = c
        step +=1
    file.close()
    finalIteration = step
    return "%d ): %.6f"%(finalIteration,c)

# Main code
def mainFunc(function, maxIteration, epsilon, a, b):
     # the possible variable names must be known beforehand...
    expr = sympify(function)
    x = var('x')

    return bisection(a, b, expr, maxIteration, epsilon, x)

