from cffi.backend_ctypes import xrange
from numpy import array, zeros, dot, diag

A = array([[4., -1., -1., 0], [-1., 4., 0., -1], [-1., 0., 4., -1], [0.,-1.,-1.,4]])
B = array([[30.], [60.], [40.], [70.]])

## Eliminación de Gauss mediante pivotaje parcial

def GEPP(A, b):
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)

    for k in xrange(n - 1):
        # Choose largest pivot element below (and including) k
        maxindex = abs(A[k:, k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        # Swap rows
        if maxindex != k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]]
        for row in xrange(k + 1, n):
            multiplier = A[row][k] / A[k][k]
            # the only one in this column since the rest are zero
            A[row][k] = multiplier
            for col in xrange(k + 1, n):
                A[row][col] = A[row][col] - multiplier * A[k][col]
            # Equation solution column
            b[row] = b[row] - multiplier * b[k]
    # print A ;print b
    x = zeros(n)
    k = n - 1
    x[k] = b[k] / A[k, k]
    while k >= 0:
        x[k] = (b[k] - dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k = k - 1
    return x
Aug = GEPP(A, B)
print('Eliminación de Gauss mediante pivotaje parcial: ans is\n', Aug)

# Back Substitution
def forward_elimination(A, b, n):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n - 1):
        for i in range(row + 1, n):
            factor = A[i, row] / A[row, row]
            for j in range(row, n):
                A[i, j] = A[i, j] - factor * A[row, j]

            b[i] = b[i] - factor * b[row]

    return A, b

def back_substitution(a, b, n):
    """"
    Realiza sustitución hacia atrás, devuelve el resultado gaussiano.
    """
    x = zeros((n, 1))
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for row in range(n - 2, -1, -1):
        sums = b[row]
        for j in range(row + 1, n):
            sums = sums - a[row, j] * x[j]
        x[row] = sums / a[row, row]
    return x
def gauss(A, b):
    """
    Esta función realiza la eliminación gaussiana sin pivotar.
    """
    n = A.shape[0]

    # Check for zero diagonal elements
    if any(diag(A) == 0):
        raise ZeroDivisionError(('Se producirá la división por cero; '
                                 'pivot actualmente no es compatible'))

    A, b = forward_elimination(A, b, n)
    return back_substitution(A, b, n)

x = gauss(A, B)
print('\n La solución se puede obtener mediante sustitución inversa:'
      '\n x1 = %i \n x2 = %i \n x3= %i \n x4= %i  \n' % (x[0], x[1], x[2], x[3]))
