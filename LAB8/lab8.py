import numpy as np
import sympy as sp
from numpy.linalg import matrix_power
#from numpy.linalg import inv

A = np.array([[4,2],
             [2,4]])

#Eigenvalores y Eigenvectores

EIG = np.linalg.eigvals(A)
print("Eigenvalores: \n " + str(EIG))
EIGV = np.linalg.eig(A)
print("Eigenvectores: \n " + str(EIGV))

#Diagonalizacion

P, D = sp.Matrix(A).diagonalize()
print("Diagonalizacion: \n ")
print("P: \n " + str(P))
print("D: \n " + str(D))


potencia=25

# A ^ potencia mediante diagonalizacion
print("Potencias de A usando diagonalización")
print("inversa de P "+ str(P**(-1)))
print("A^"+str(potencia)+": \n" + str((P)* (D**potencia)* P**(-1) ) )

# Potencias de A usando matrix power
print("Potencias de A usando matrix power")
print("A^"+str(potencia)+": \n" + str(matrix_power(A,potencia)))


