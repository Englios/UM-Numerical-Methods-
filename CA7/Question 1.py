import numpy as np
import matplotlib.pyplot as mpl


def f(x):
    return x * np.log(x)


a = 1.0
b = 2.0

midpoint = (b - a) * f((a + b) / 2)

trapezoid = (b - a) / 2 * (f(a) + f(b))

simpson = (b - a) / 6 * (f(a) + 4 * f(a + b / 2) * f(b))

exact = 0.63662943610

print(midpoint, trapezoid, simpson, exact)

x = np.linspace(1, 2)

mpl.plot(x, f(x), label="$f(x)=x ln x")
mpl.fill_between(x, 0, f(x), alpha=0.5)
mpl.show()
