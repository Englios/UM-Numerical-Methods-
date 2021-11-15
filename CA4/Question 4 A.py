# Write a computer program that uses Newton’s-Raphson method to find the root
# of the given function. Stop the iteration when the error estimated by Δx is less
# than 10 ** -6

# definition of the newton raphson method for future use
def newtonraphson(f, fp, xo, tol):
    x1 = xo - f(xo) / fp(xo)
    error = abs(x1 - xo)
    i = 0
    while error >= tol:
        error = abs(x1 - xo)
        print("||Iteration number {0:2d}||".format(i + 1))
        print("|| X[{3:2d}] Value:{0:10.10f} "
              "|| X[{4:2d}] Value:{1:10.10f} "
              "|| Error Value:{2:10.10f} || \n"
              .format(xo, x1, error, i, i + 1))
        xo = x1
        x1 = xo - f(xo) / fp(xo)
        i += 1
    return "\n"


# intializing the formulas in newton-raphson method
f = lambda x: x ** 3 - 2 * x - 5
fp = lambda x: 3 * x ** 2 - 2

# Intializing tolerance value
tol = 10 ** -6
# Initilizing the initial x value
xo = 2

#Recalling the Newton Raphson
newtonraphson(f, fp, xo, tol)
