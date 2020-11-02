"""
Algebra Lineal - Lab 8
Entrega: 11/2/2020
@steven_wilson
"""

import numpy as np
import sympy as sp
from numpy.linalg import matrix_power
#from numpy.linalg import inv


# A

A = np.array([[6, -1],
              [2, 3]])

# Eigenvalores y Eigenvectores

EIG = np.linalg.eigvals(A)
print("\nMATRIZ A\nEigenvalores: A\n " + str(EIG))

# Diagonalizacion

P, D = sp.Matrix(A).diagonalize()
print("Diagonalizacion A: \n ")
print("P: \n " + str(P))
print("D: \n " + str(D))

potencia = 10

# A ^ potencia mediante diagonalizacion
print("Potencias de A usando diagonalizacion")
print("inversa de P " + str(P**(-1)))
print("A^"+str(potencia)+": \n" + str((P) * (D**potencia) * P**(-1)))

# Potencias de A usando matrix power
print("Potencias de A usando matrix power")
print("A^"+str(potencia)+": \n" + str(matrix_power(A, potencia)))


# B

B = np.array([[2, 0, 0],
              [1, 2, 1],
              [-1, 0, 1]])

# Eigenvalores y Eigenvectores

EIG = np.linalg.eigvals(B)
print("\nMATRIZ B\nEigenvalores: B\n " + str(EIG))

# Diagonalizacion

P, D = sp.Matrix(B).diagonalize()
print("\nDiagonalizacion B: \n ")
print("P: \n " + str(P))
print("D: \n " + str(D))

potencia = 10

# B ^ potencia mediante diagonalizacion
print("Potencias de B usando diagonalizacion")
print("inversa de P " + str(P**(-1)))
print("B^"+str(potencia)+": \n" + str((P) * (D**potencia) * P**(-1)))

# Potencias de A usando matrix power
print("Potencias de B usando matrix power")
print("B^"+str(potencia)+": \n" + str(matrix_power(B, potencia)))


# C

C = np.array([[1, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0]])

# Eigenvalores y Eigenvectores

EIG = np.linalg.eigvals(C)
print("\nMATRIZ C\nEigenvalores: C\n " + str(EIG))

# Diagonalizacion

P, D = sp.Matrix(A).diagonalize()
print("Diagonalizacion C: \n ")
print("P: \n " + str(P))
print("D: \n " + str(D))

potencia = 10

# A ^ potencia mediante diagonalizacion
print("Potencias de C usando diagonalizacion")
print("inversa de P " + str(P**(-1)))
print("C^"+str(potencia)+": \n" + str((P) * (D**potencia) * P**(-1)))

# Potencias de A usando matrix power
print("Potencias de A usando matrix power")
print("A^"+str(potencia)+": \n" + str(matrix_power(C, potencia)))
