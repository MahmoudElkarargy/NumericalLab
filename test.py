
# Python program for implementation
# of Bisection Method for
# solving equations


# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2 + 2

from sympy import var
from sympy import sympify

def func(expr, value):
	return expr.subs(x, value)


# Prints root of func(x)
# with error of EPSILON
def bisection(a,b,expr):
    if (func(expr,a) * func(expr,b) >= 0):
        print("You have not assumed right a and b\n")
        return
    c = a
    step = 0
    while ((b-a) >= Epsilon and step < maxIteration):
    	# Find middle point
        c = (a+b)/2

		# Check if middle point is root
        if (func(expr,c) == 0.0):
	        break

		# Decide the side to repeat the steps
        if (func(expr,c)*func(expr,a) < 0):
            b = c
        else:
            a = c
        step +=1
    print("The value of root is : ","%.4f"%c)

# Main code
#take from the user function.
x = var('x')  # the possible variable names must be known beforehand...
function = input("Enter your function: ")
expr = sympify(function)

# Take from user assumtion of a and b.
a = int(input("Enter your assumtion for lower bond: "))
b = int(input("Enter your assumtion for upper bond: "))

maxIteration = int(input("Enter max number of Iterations: "))
Epsilon = float(input("Enter Epsilon: "))


bisection(a, b, expr)



# from sympy import *
#
#
# # Defining Function
# def f(y):
#     x = var('x')
#     return Function.subs(x, y)
#
#
# # Implementing Secant Method
#
# def secant(x0, x1, e, N):
#     print('\n\n*** SECANT METHOD IMPLEMENTATION *')
#     step = 1
#     condition = True
#     while condition:
#         if f(x0) == f(x1):
#             print('Divide by zero error!')
#             break
#
#         x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
#         print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
#         x0 = x1
#         x1 = x2
#         step = step + 1
#
#         if step > N:
#             print('Not Convergent!')
#             break
#
#         condition = abs(f(x2)) > e
#     print('\n Required root is: %0.8f' % x2)
#
#
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))
# expr = input('please enter equation: ')
# Function = sympify(expr)
#
# # Starting Secant Method
# secant(x0, x1, e, N)