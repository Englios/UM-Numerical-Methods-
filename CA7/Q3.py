import numpy as np
import matplotlib.pyplot as mpl


# define the energy formula
def f(E):
    T = 10 ** 7
    e = 10 ** 6
    k = 8.6174 * 10 ** -11
    Za = 2
    Zb = 2
    fine_structure = 1.439976
    G = fine_structure * ((Za * Zb) / e)  # Definition of Gamow factor;- It has to be constant
    return np.exp(-2 * G) * np.exp(-E / (k * T))


# Initialize Lower Integral Value:- The value cannot be 0 therefore we took it to be a value Nearing 0
a = 10 ** -200

# Initialize Upper Integral Value:- The value cannot be infinite therefore we took it to be a value
# Nearing infinity

b = 10 ** 200

# Calculations
trapezoid = (b - a) / 2 * (f(a) + f(b))  # Basic Trapezoidal RUle

simpson = (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))  # Basic Simpsons rule

print("\n\nBasic Trapezoid Value = {0:15.10f} \n\nBasic Simpson Value = {1:15.10f} "
      .format(trapezoid, simpson))

# Graphing the Output

x = np.linspace(a, b, 10000)

mpl.plot(x, f(x), label="f(x)")
mpl.fill_between(x, 0, f(x), alpha=0.5)
mpl.legend()
mpl.show()
