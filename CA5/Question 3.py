# Use Doolittle's Method to find solve the circuit
# Loop 1 25x1-10x2=-90
# Loop2 -10x1+40x2=180


import scipy.linalg
import numpy as np

float_formatter='{:.2f}'.format
np.set_printoptions(formatter={'float_kind':float_formatter})

A = np.array([[25.00, -10.00], [-10.00, 40.00]])
B = np.array([[-90.00], [180.00]])

P, L, U = scipy.linalg.lu(A)

print("A matrix:\n", A)
print("\nL matrix:\n", L)
print("\nU matrix:\n", U)

Y = scipy.linalg.solve(L, B)
X = scipy.linalg.solve(U, Y)

print("\nLU\n",np.dot(L,U))
print("\nY value\n", Y)
print("\nX value\n", X)
print()
print("I1 value = {} A".format(X[0]),
      "\nI2 Value = {} A".format(X[1]))
