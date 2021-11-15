import numpy as np


def midpointcomp(f, a, b, N):
    if N <= 0:
        raise ValueError("N must be more than 0.")
    dx = (b - a) / N
    i = np.linspace(1, N, N)
    y = f(a + (i - 1 / 2) * dx)
    M = dx * np.sum(y)
    return M


def trapezoidcomp(f, a, b, N):
    if N <= 0:
        raise ValueError("N must be more than 0.")
    h = (b - a) / N
    x = np.linspace(a, b, N - 1)
    T = h*(0.5 * f(a) + np.sum(f(x)) + 0.5 * f(b))
    return T


def simpscomp(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S


def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    result = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


f = lambda x: x * np.log(x)
exact = 0.63662943610

print(midpointcomp(f, 1, 2, 5))
print(trapezoidcomp(f, 1, 2, 5))
print(simpscomp(f, 1, 2, 5 + 1))
print(trapezoidal(f, 1, 2, 5))
