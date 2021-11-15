import numpy as np
import matplotlib.pyplot as mpl


def f(E):
    finestructure = 1.439976
    Za = 2
    Zb = 2
    k = 8.6174 * 10 ** -11
    T = 10 ** 7
    epsilon = 8.854 * 10 ** -12
    G = finestructure * ((Za * Zb) / 10 ** 6)
    return np.exp(-2 * G) * np.exp(-E / (k * T))


a = 10 ** -100
b = 10 ** 100

midpoint = (b-a)*f((a+b)/2)

trapezoid = (b - a) / 2 * (f(a) + f(b))

simpson = (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

print("Midpoint Value || {0:15.10f} \n\nTrapezoid Value || {1:15.10f} \n\nSimpson Value || {2:15.10f} "
      .format(midpoint, trapezoid, simpson))

print(midpoint)

x = np.linspace(a, b, 100000)

mpl.plot(x, f(x), label="f(x)")
mpl.fill_between(x, 0, f(x), alpha=0.5)
mpl.legend()
mpl.show()
