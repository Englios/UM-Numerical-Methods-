# For each following functions, do a calculation by hand to find the root to an
# accuracy of 0.1.

def bisection(f, a, b, tol):
    error = abs(b - a)
    c = (b + a) / 2
    i = 0
    if f(c) == 0:
        print("Root value is {0:5f}".format(c))

    else:
        if f(a) * f(b) < 0:
            print("The Interval is acceptable"
                  "\n"
                  "A Root Exists"
                  "\n")
            while error > tol:
                error = abs(b - a)
                c = (b + a) / 2
                print("||Iteration number {0:2d}||".format(i))
                print("|| A[{4:2d}] Value:{0:8.5f} "
                      "|| B[{4:2d}] Value:{1:8.5f} "
                      "|| Midpoint[{4:2d}] Value:{2:8.8f} "
                      "|| Error[{4:2d}] Value:{3:8.8f} || \n"
                      .format(a, b, c, error, i))
                i += 1
                if f(c) == 0:
                    print("\nFinal root is :{0:5.8f}".format(c))
                elif f(c) * f(a) < 0:
                    b = c
                else:
                    a = c
    return ("\n")


def newtonraphson(f, fp, xo, tol):
    x1 = xo - f(xo) / fp(xo)
    error = abs(x1 - xo)
    i = 0
    while error > tol:
        print("||Iteration number {0:2d}||".format(i + 1))
        print("|| X[{3:2d}] Value:{0:8.5f} "
              "|| X[{4:2d}] Value:{1:8.5f} "
              "|| Error Value:{2:8.8f} || \n"
              .format(xo, x1, error, i, i + 1))
        xo = x1
        x1 = xo - f(xo) / fp(xo)
        error = abs(x1 - xo)
        i += 1
    return ("\n")


def secant(f, a, b, tol):
    error = abs(b - a)
    i = 0

    if f(a) * f(b) >= 0:
        print("Secant Method Fails")

    else:
        if f(a) * f(b) < 0:
            print("The Interval is acceptable"
                  "\n"
                  "A Root Exists"
                  "\n")
            while error >= tol:
                error = abs(b - a)
                c = b - f(b) * ((b - a) / (f(b) - f(a)))
                print("||Iteration number {0:2d}||".format(i + 1))
                print("|| X[{4:2d}] Value:{0:8.5f} "
                      "|| X[{5:2d}] Value:{1:8.5f} "
                      "|| X[{6:2d}] Value:{2:8.8f} "
                      "|| Error[{4:2d}] Value:{3:8.8f} || \n"
                      .format(a, b, c, error, i, i + 1, i + 2))
                a = b
                b = c
                i += 1

                print("Final Root Value is ",c)

    return "\n"


# print(bisection(lambda x: x ** 6 - x - 1, 1, 2, 10 ** -6))
# print(newtonraphson(lambda x: x ** 6 - x - 1, lambda x: 6 * x ** 5 - 1, 2, 10 ** -6))
print(secant(lambda x: x ** 6 - x - 1, 1, 2, 0.01))
