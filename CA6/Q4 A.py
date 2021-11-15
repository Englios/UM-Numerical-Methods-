import matplotlib.pyplot as mpl


def f(x, y, i):
    return 1 - 4 * y[i]


n = 100
h = 1 / n
y = [0.00] * (n + 2)
yp = [0.00] * (n + 2)
x = [0.00] * (n + 2)
ypp = [0.00] * (n + 2)
ycc = [0.00] * (n + 2)
y[0] = 1 / 2
x[0] = 0
ycc[0] = y[0]
ypp[0] = y[0]

print("Euler's Method")
for i in range(0, n + 1):
    yp[i] = f(x, y, i)
    y[i + 1] = y[i] + h * f(x, y, i)
    x[i + 1] = x[i] + h
    print("I Value: {0:2d} || X Value:{1:5.2f} || Y Value:{2:5.5f} || Y' Value:{3:5.5f} || Yp Value:{4:5.5f}"
          .format(i, x[i], y[i], y[i + 1], yp[i]))

print("\nPredictor")
for i in range(0, n + 1):
    ypp[i + 1] = y[i] + h / 24 * (55 * yp[i] + 59 * yp[i - 1] + 37 * yp[i - 2] - 9 * yp[i - 3])
    print("I Value: {0:2d} || X Value:{1:5.2f} || Ypp Value:{2:5.5f}".format(i, x[i], ypp[i]))

print("\nCorrector")
for i in range(0, n + 1):
    ycc[i + 1] = y[i] + h / 24 * (9 * ypp[i + 1] - 19 * yp[i] + 5 * yp[i - 1] - yp[i - 2])
    print("I Value: {0:2d} || X Value:{1:5.2f} || Ycc Value:{2:5.5f}".format(i, x[i], ycc[i]))

print(y)

mpl.plot(x[0:n + 1], y[0:n + 1], 'k.-', label="Euler's Methods", markersize=2)
mpl.plot(x[0:n + 1], ypp[0:n + 1], 'b--', label="Adam-BashFord Predictor", markersize=2)
mpl.plot(x[0:n + 1], ycc[0:n + 1], 'c--', label="Adam-BashFord Corrector", markersize=2)
mpl.legend()
mpl.show()
