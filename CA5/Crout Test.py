import numpy as np

float_formatter = "{:.3f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})


def Crout(a, b):
    cout = 0
    m, n = a.shape
    if (m != n):
        print("Crout cannot be used.")  # Ensure that the number of equations is equal to the number of unknowns
    else:
        l = np.zeros((n, n))
        u = np.zeros((n, n))
        s1 = 0
        s2 = 0

        for i in range(n):
            l[i][0] = a[i][0]
            u[i][i] = 1
        for j in range(1, n):
            u[0][j] = a[0][j] / l[0][0]
        for k in range(1, n):
            for i in range(k, n):
                for r in range(k): s1 += l[i][r] * u[r][k]
                l[i][k] = a[i][k] - s1
                s1 = 0  # Initialize s1 after each summation=0
            for j in range(k + 1, n):
                for r in range(k): s2 += l[k][r] * u[r][j]
                u[k][j] = (a[k][j] - s2) / l[k][k]
                s2 = 0  # Initialize s2 after each summation=0
        print("U Matrix \n", u)
        print()
        print("L Matrix \n", l)
        print()
        print("\nL times U\n", np.dot(l, u))
        print()

        #
        y = np.zeros(n)
        s3 = 0
        y[0] = b[0] / l[0][0]  # First calculate the first x solution
        for k in range(1, n):
            for r in range(k):
                s3 += l[k][r] * y[r]
            y[k] = (b[k] - s3) / l[k][k]
            s3 = 0

            # Back generation to solve
        x = np.zeros(n)
        s4 = 0
        x[n - 1] = y[n - 1]
        for k in range(n - 2, -1, -1):
            for r in range(k + 1, n):
                s4 += u[k][r] * x[r]
            x[k] = y[k] - s4
            s4 = 0

        for i in range(n):
            print("x" + str(i + 1) + " = ", x[i])
        print("x" " = ", x)


if __name__ == '__main__':  # When the module is run directly, the following code blocks will be run. When
    # the module is imported, the code blocks will not be run.
    a = np.array([[2, 4, 2, 6, 7], [4, 9, 6, 15, 7], [2, 6, 9, 18, 7], [6, 15, 18, 40, 7], [1, 5, 6, 100, 7]])
    b = np.array([9, 23, 22, 47, 69])
    Crout(a, b)
