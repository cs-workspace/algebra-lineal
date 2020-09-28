"""
Algebra Lineal - Lab6
Entrega: 9/28/2020
@steven_wilson
"""

import numpy as np
import sympy as sp
from scipy.linalg import null_space


A = sp.Matrix([[1, 0, -1],
               [1, 1, 1]])

B = sp.Matrix([[1, 1, -1],
               [1, 5, 1],
               [1, -1, -2]])

C = sp.Matrix([[1, 1, 0, 1],
               [0, 1, -1, 1],
               [0, 1, -1, -1]])

D = sp.Matrix([[2, -4, 0, 2, 1],
               [-1, 2, 1, 2, 3],
               [1, -2, 1, 4, 4]])

print(A)
print('\n', B)
print('\n', C)
print('\n', D)

# Encontrar el rango
RangoA = np.linalg.matrix_rank(np.array(A).astype(np.float64))
RangoB = np.linalg.matrix_rank(np.array(B).astype(np.float64))
RangoC = np.linalg.matrix_rank(np.array(C).astype(np.float64))
RangoD = np.linalg.matrix_rank(np.array(D).astype(np.float64))

print("\n El rango de A es: "+str(RangoA))
print("\n El rango de B es: "+str(RangoB))
print("\n El rango de C es: "+str(RangoC))
print("\n El rango de D es: "+str(RangoD))


# Encontrar la nulidad
num_rows, num_cols = np.array(A).astype(np.float64).shape
nulidadA = num_cols-RangoA

num_rows, num_cols = np.array(B).astype(np.float64).shape
nulidadB = num_cols-RangoB

num_rows, num_cols = np.array(C).astype(np.float64).shape
nulidadC = num_cols-RangoC

num_rows, num_cols = np.array(D).astype(np.float64).shape
nulidadD = num_cols-RangoD

print("\n La nulidad de A es: " + str(nulidadA))
print("\n La nulidad de B es: " + str(nulidadB))
print("\n La nulidad de C es: " + str(nulidadC))
print("\n La nulidad de D es: " + str(nulidadD))


# Encontrar el espacio Nulo
EspacioNuloA = A.nullspace()
EspacioNuloB = B.nullspace()
EspacioNuloC = C.nullspace()
EspacioNuloD = D.nullspace()

print("\n El espacio nulo de A es: \n "+str(EspacioNuloA))
print("\n El espacio nulo de B es: \n "+str(EspacioNuloB))
print("\n El espacio nulo de C es: \n "+str(EspacioNuloC))
print("\n El espacio nulo de D es: \n "+str(EspacioNuloD))
