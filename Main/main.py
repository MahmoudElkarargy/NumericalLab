import Methods.Bisection as Bisection
# import Methods.RegularFalse as RegularFalse
# import Methods.Secant as Secant

print("\n1- Bisection Method\t 2- Regular False Method\n3- Secant Method")
method = input("\nPlease select your method:  ")

if method == "1":
    print("\nYou choosed Bisection Method")
    Bisection.mainFunc()

if method == "2":
    print("\nYou choosed Regular False Method")

if method == "3":
    print("\nYou choosed Secant Method")