def f(x, y):
    return 1 - 4 * y


x = 0
y = 1
n = 2
h = 1 / n
k1 = f(x, y)
k2 = f(x + h, y + h * k1)

for i in range(n + 1):
    y1 = y + h / 2 * (k1 * k2)
    print(" X Value: {0:6.2f} || Y Value: {1:6.5f} || Yp Value: {2:6.5f}".format(x, y, y1))
    x = x + h
    y = y1
