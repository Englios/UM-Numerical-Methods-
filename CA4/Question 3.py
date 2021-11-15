# The author needs to borrow RM150,000 to buy a new house that he wants and he can afford to pay only RM600 per
# month. Assuming 30-year mortgage, use bisection method to determine what interest rate he can afford to pay. Write
# a computer program to calculate the interest rate. L=150000,M=600,m=12 Find r

import matplotlib.pyplot as mpl
import numpy as np


# Define the Interest rate formula
def f(r):
    L = 150000
    M = 600
    m = 30
    return (12 * M) / r * (1 - (1 + (r / 12)) ** (-12 * m)) - L


a = 0.01
b = 0.2
c = (b + a) / 2
error = abs(b - a)
i = 0

x = np.linspace(a, b, 10000)

# check to see if the C value is a root or not
if f(c) == 0:
    print("Root value is {0:5f}".format(c))

else:
    if f(a) * f(b) < 0:  # Check for interval
        print("The Interval is acceptable"
              "\n"
              "A Root Exists"
              "\n")
        while f(c) != 0:  # Printing the values
            error = abs(b - a)
            c = (b + a) / 2
            print("||Iteration number {0:2d}||".format(i))
            print("|| A[{4:2d}] Value:{0:8.5f} "
                  "|| B[{4:2d}] Value:{1:8.5f} "
                  "|| Midpoint[{4:2d}] Value:{2:20.32f} "
                  "|| Error[{4:2d}] Value:{3:20.32f} || \n"
                  .format(a, b, c, error, i))
            i += 1
            if f(c) == 0:  # return Final interest rate
                print("\nFinal Interest Rate is :{0:5.8f}".format(c))
            elif f(c) * f(a) < 0:  # Change the value of b to c
                b = c
            else:  # Change the value of a to c
                a = c
            mpl.plot(c, f(c), '.', markersize=10)

        # Plotting the graph
        mpl.plot(x, f(x), 'k--', label='Interest Equation')
        mpl.text(0.05, 20000, r'$Each\ iteration\ of\ the\ midpoint\ is\ shown\ in\ colour$')

        mpl.xlabel('x')
        mpl.ylabel('f (x)')
        mpl.legend()
        mpl.show()

    else:
        print("The interval cannot be used")
