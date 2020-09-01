"""
Algebra Lineal - Lab3
Entrega: 31/8/20
@steven_wilson
"""

import numpy as np
import sympy as sp

# 1. Matrices A y B tamano 15 x 15 numeros aleatorios entre (-10, 10)
A = np.random.randint(-10, 10, size=(15, 15))
B = np.random.randint(-10, 10, size=(15, 15))
print('Matriz A:\n', A)
print('\nMatriz B:\n', B)

# 2. Suma de matrices del mismo tamano
sum_matrices = A + B
print('\nSuma de A + B:\n',  sum_matrices)


# 3. Diferencia de matrices del mismo tamano
dif_matrices = A - B
print('\nDiferencia de A - B:\n',  dif_matrices)


# 4. Producto componente por componente entre A y B.
producto_cxc = A * B
print('\nProducto componente por componente AB:\n', producto_cxc)


# 5. Producto Matricial BA
producto_matrices = B.dot(A)
print('\nProducto Matricial de BA:\n', producto_matrices)


# 6. FERR A
ferr_A = sp.Matrix(A).rref()
print('\nFERR A:\n', ferr_A)


# 7. FERR B
ferr_B = sp.Matrix(B).rref()
print('\nFERR B:\n', ferr_B)
