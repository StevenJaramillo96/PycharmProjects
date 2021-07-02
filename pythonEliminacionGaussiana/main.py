import numpy as np
A = np.array([[4, -1, -1, 0],
              [-1, 4, 0, -1],
              [-1, 0, 4, -1],
              [0,-1, -1, 4]])
b = np.array([30, 60, 40, 70])
np.linalg.det(A)
n = np.ndim(A)
N = len(b)
print("la matriz ingresada:\n", A)
def EliminacionGaussiana(A, b):
    n = np.size(b)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            mult = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= mult * A[k, j]
            b[i] -= mult * b[k]

for i in range(N - 1):
    b[i] = b[i] / A[i][i]
    A[i] = A[i] / A[i][i]
    print(A, b)
    print('---------------------------------------------')
    for k in range(i + 1, N):
        b[k] = b[k] - A[k][i] * b[i]

        A[k] = A[k] - A[k][i] * A[i]
    print(A, b)
    print('---------------------------------------------')

i = N - 1
b[i] = b[i] / A[i][i]
A[i] = A[i] / A[i][i]

print(A, b)
