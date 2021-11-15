import numpy as np


def simpscomp(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S


def simpson(f, a, b):
    S = (b - a) / 6 * (f(a) + 4 * f((b + a) / 2) + f(b))
    return S


exact = 0.636629

S1 = simpson(lambda x: x*np.log(x), 2, 1)
S2 = simpscomp(lambda x: x*np.log(x), 2, 1,4)
error1 = abs(exact - S1)
error2 = abs(exact - S2)

print("Using Simpson Rule :", S1,
      "\nError :", error1)
print("Using Simpson Composite Rule :", S2,
      "\nError :", error2)
