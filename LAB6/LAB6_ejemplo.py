import numpy as np
import sympy as sp
from scipy.linalg import null_space


A = sp.Matrix([[1, 3, 1, 4],
               [2, 9, 4, 9],
               [1, 0, -1, 3]])

print(A)

# Encontrar el rango
RangoA = np.linalg.matrix_rank(np.array(A).astype(np.float64))
print("El rango de A es: "+str(RangoA))

# Encontrar la nulidad
num_rows, num_cols = np.array(A).astype(np.float64).shape
nulidadA = num_cols-RangoA
print("La nulidad de A es: " + str(nulidadA))

# Encontrar el espacio Nulo
EspacioNuloA = A.nullspace()
print("El espacio nulo de A es: \n "+str(EspacioNuloA))
