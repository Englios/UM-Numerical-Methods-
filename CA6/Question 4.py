def f(x, y, i):
    return 1 - 4 * y[i]

n = 4
h = 1 / n
y = [0.00] * (n + 2)
yp = [0.00] * (n + 2)
x = [0.00] * (n + 2)
ypp = [0.00] * (n + 2)
ycc = [0.00] * (n + 3)
y[0] = 1 / 2
x[0] = 0

print("Euler's Method")
for i in range(0, n + 1):
    y[i + 1] = y[i] + h * f(x, y, i)
    x[i + 1] = x[i] + h
    print("I Value:-{0:2d} || X Value:-{1:5.2f} || Y Value:-{2:5.5f} || Yp Value:-{3:5.5f}".format(i, x[i], y[i], y[i+1]))

print("\nPredictor")
for i in range(0, n + 1):
    ypp[i + 1] = y[i] + h / 24 * (55 * yp[i - 1] + 37 * yp[i - 2] - 9 * yp[i - 3])
    print("I Value:-{0:2d} || X Value:-{1:5.2f} || Ypp Value:-{2:5.5f}".format(i, x[i], ypp[i]))

print("\nCorrector")
for i in range(0, n + 1):
    ycc[i + 1] = y[i] + h / 24 * (9 * ypp[i + 1] - 19 * yp[i] + 5 * yp[i - 1] - yp[i - 2])
    print("I Value:-{0:2d} || X Value:-{1:5.2f} || Ypp Value:-{2:5.5f}".format(i, x[i], ycc[i]))
