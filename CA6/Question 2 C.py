import numpy as np
import matplotlib.pyplot as mpl


def f(x, y, i):
    p=1.41
    return p*4*np.pi*(x[i]**2)


n = 4
h = 1 / n
y = [0.00] * (n + 2)
x = [0.00] * (n + 2)
y[0] = 0
x[0] = 0
i = 0
z = np.linspace(0, 1,100)
exact = np.exp(np.log(3) * np.exp(-z))

for i in range(n + 1):
    y[i + 1] = y[i] + h * f(x, y, i)
    x[i + 1] = x[i] + h

    print("Iteration Number {0:2d}"
          "\n"
          "||I = {0:2d} "
          "|| X[{0:2d}] Value = {2:5.4f}"
          "|| Y[{0:2d}] Value = {3:5.4f}"
          "|| Y[{1:2d}] Value = {4:5.4f}"
          "\n"
          .format(i, i + 1, x[i], y[i], y[i + 1]))

mpl.ylabel("F(x)")
mpl.xlabel("X")
# mpl.scatter(x[0:n+1], y[0:n+1],label="Euler's Method",marker='.',color='r')
mpl.plot(x[0:n+1], y[0:n+1],'c-' ,label="Euler's Method when n={0}".format(n), markeredgecolor='r', marker='.')
mpl.plot(z, exact, "k", label='Exact Solution',alpha=0.5)
mpl.legend()
mpl.show()
