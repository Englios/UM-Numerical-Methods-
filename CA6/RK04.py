def f(x, y):
    return 1 - 4 * y

x = 0
y = 1
n = 10
h = 1 / n
k1 = f(x, y)
k2 = f(x + h/2, y + h/2 * k1)
k3 = f(x + h/2, y + h/2 * k2)
k4 = f(x+h, y+h*k3)


for i in range(n + 1):
    y1 = y + h / 2 * (k1+2*k2+2*k3+k4)
    print(" X Value: {0:6.2f} || Y Value: {1:6.5f} || Yp Value: {2:6.5f}".format(x, y, y1))
    x = x + h
    y = y1
